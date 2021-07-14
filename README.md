# sendmail
Small python CLI to send mail through your shell

Don't forget to configure and rename `.env.example`.

```
usage: sendmail.py [-h] -t TO [-s SUBJECT] -m MESSAGE

Send plaintext emails.

optional arguments:
  -h, --help            show this help message and exit
  -t TO, --to TO        Receiver email address.
  -s SUBJECT, --subject SUBJECT
                        Subject of message.
  -m MESSAGE, --message MESSAGE
                        Message to send.
```