#!/usr/bin/env python3
"""
Standalone SES sandbox test.

Sends a raw email (with a tiny PDF attachment) from a verified sender to a
verified recipient. Both must be verified identities in the SAME region,
because your account is still in the SES sandbox.

Run:
    export AWS_REGION=us-east-1
    export SES_SENDER=you@example.com          # must be a VERIFIED identity
    export SES_RECIPIENT=someone@example.com   # in sandbox, must ALSO be verified
    # creds resolve from ~/.aws or your current role (PowerUser is fine)
    python mail_test.py

Expected: prints a MessageId and the mail lands in the recipient's inbox.
"""

import os
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.application import MIMEApplication

import boto3
from botocore.exceptions import ClientError

# ---- configure via environment variables -----------------------------------
SENDER    = os.environ["SES_SENDER"]      # must be a VERIFIED identity
RECIPIENT = os.environ["SES_RECIPIENT"]   # in sandbox, must ALSO be verified
REGION    = os.environ.get("AWS_REGION", "us-east-1")
# ----------------------------------------------------------------------------


def _tiny_pdf() -> bytes:
    """Smallest valid PDF — no reportlab needed, just proves attachments work."""
    return (
        b"%PDF-1.4\n"
        b"1 0 obj<</Type/Catalog/Pages 2 0 R>>endobj\n"
        b"2 0 obj<</Type/Pages/Kids[3 0 R]/Count 1>>endobj\n"
        b"3 0 obj<</Type/Page/Parent 2 0 R/MediaBox[0 0 200 200]>>endobj\n"
        b"xref\n0 4\n0000000000 65535 f \n0000000009 00000 n \n"
        b"0000000052 00000 n \n0000000101 00000 n \n"
        b"trailer<</Size 4/Root 1 0 R>>\nstartxref\n164\n%%EOF"
    )


def main() -> None:
    ses = boto3.client("ses", region_name=REGION)

    msg = MIMEMultipart()
    msg["Subject"] = "SES sandbox test — HomeLoanAgent"
    msg["From"] = SENDER
    msg["To"] = RECIPIENT
    msg.attach(MIMEText(
        "If you're reading this, SES sandbox sending works end to end.\n"
        "The attached PDF confirms raw-email attachments also work.",
        "plain", "utf-8",
    ))

    part = MIMEApplication(_tiny_pdf(), _subtype="pdf")
    part.add_header("Content-Disposition", "attachment", filename="test.pdf")
    msg.attach(part)

    try:
        resp = ses.send_raw_email(
            Source=SENDER,
            Destinations=[RECIPIENT],
            RawMessage={"Data": msg.as_string()},
        )
        print(f"✅ sent — MessageId={resp['MessageId']}")
        print(f"   {SENDER} → {RECIPIENT} in {REGION}")
    except ClientError as e:
        code = e.response["Error"]["Code"]
        msg_ = e.response["Error"]["Message"]
        print(f"❌ {code}: {msg_}")
        if code == "MessageRejected" and "not verified" in msg_:
            print("\n→ Sandbox rule: the RECIPIENT must also be a verified "
                  "identity. Verify it in SES → Identities, or request "
                  "production access.")
        elif "Region" in msg_ or code == "InvalidClientTokenId":
            print(f"\n→ Check that both identities are verified in {REGION} "
                  "and your creds point at the right AWS account.")


if __name__ == "__main__":
    main()