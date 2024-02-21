#!/bin/bash

send_mail(){
	#Get the recipient, subject and the message body
	newline=$'\n'
	regexpattern=^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$
	local recipientaddress subject message

	read -p "Enter recipient email address:${newline}" recipientaddress
		
	if [[ $recipientaddress =~ $regexpattern ]]; then
		read -p "Enter email's subject:${newline}" subject
		read -p "Enter email's body:${newline}" message
		#Checking if the message and subject exists
		if [ -z "$subject" ] && [ -z "$message" ]; then
			echo "Provide subject and the body message!!"
			send_mail
		fi
	else
		echo "Please enter a valid email address!!"
		send_mail
	fi	

	#sending of the mail
	{ 	
		echo "subject:$subject"
		echo  "$message" 
	} | /usr/sbin/ssmtp "$recipientaddress"

	#checking if mail was sent successful
	 if [ $? -eq 0 ]; then
	        echo "Email has been sent successfully to $recipientaddress"
	 else
        	echo "Failed to send email."
	        return 1
	 fi

}
send_mail
