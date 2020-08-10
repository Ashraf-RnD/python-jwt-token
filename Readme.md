 Private Key generation
 
     openssl rsa -in mykey.pem -out rnd-public-key.pub -pubout
 
 Public Key Generation
 
     openssl rsa -in rnd-private-key.pem -out rnd-public-key.pub -pubout