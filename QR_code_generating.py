import qrcode

# Taking UPI ID as a input from the user

upi_id = input("Enter your UPI ID = ")

#upi://pay?pa=UPI_OD&pn=NAME&am=Amount&cu=CURRENCY&tn=MESSAGE

# Defining the payment UPL based on thr UPI ID and the payment app 
#you can modify these URLs based on the payment apps you wnat to support 

phonepe_url = f'upi://pay?pa={upi_id}&pn=Racipients%20Name&mc=1234'
paytm_url = f'upi://pay?pa={upi_id}&pn=Racipients%20Name&mc=1234'
google_pay_url = f'upi://pay?pa={upi_id}&pn=Racipients%20Name&mc=1234'

#create OR codes for each payment app

phonepe_qr = qrcode.make(phonepe_url)
paytm_qr = qrcode.make(paytm_url)
google_qr = qrcode.make(google_pay_url)

#save the QR code to image file (optional)
phonepe_qr.save("phonepe_qr.png")
paytm_qr.save("paytm_qr.png")
google_qr.save("google_pay_qr.png")


# Display the QR cods( you may need to install pillow library)

phonepe_qr.show()
paytm_qr.show()
google_qr.show()
