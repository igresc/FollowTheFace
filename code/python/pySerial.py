import serial

Arduino_Serial = serial.Serial('com3', 9600)
ret = Arduino_Serial.readline()
print(ret.decode())

while True:                                      
    input_data = input("Enter nº steps: ")
    print("You entered: ", input_data)
    input_data = input_data.encode('utf-8')
    Arduino_Serial.write(input_data)
    
    ret = Arduino_Serial.readline()
    print(ret.decode())
