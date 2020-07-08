Using this program you can find whether your password is exposed in data breaches or not.
This program uses the API of "haveibeenpwned.com" 

Why it is better to use this program instead of website?
WEBSITE:
 	You have to enter your whole password in their website to find whether your password is breached or not. This raises a privacy issue.
PROGRAM:
 	In this program we HASH encode the password we want to check and use only the first 5 characters of the HASHED password(it has 38 characters). 
 	we use the first 5 characters thru the website API and find the LIST of HASHED password which matches our first 5 characters.
 	Finally with the extracted list we use our password to check whether it is breached or not.
 	By this way our password will not be revealed to any server/application outside our system.
 	To make it more secure instead of sending the password(Which needs to be checked) thru cmd, we created a seperate file where it contains password or list of passwords which needs to be checked. 
