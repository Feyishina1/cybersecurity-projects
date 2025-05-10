A Python script to check the strength of a password based on:

    Minimum 8 characters

    At least 1 uppercase letter

    At least 1 lowercase letter

    At least 1 digit

    At least 1 special character
Example Tests:
Password	Result
password	Weak: No uppercase letter, etc.
Password1	Weak: No special character
Password!	Weak: No digit
Pass!23	Weak: Less than 8 characters
Password1!	Strong password

