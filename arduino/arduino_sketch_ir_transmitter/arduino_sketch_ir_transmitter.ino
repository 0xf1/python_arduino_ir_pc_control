#define DECODE_NEC          1
#include <IRremote.h>


//IRremote library https://github.com/Arduino-IRremote/Arduino-IRremote (install from Library Manager of Arduino Ide)

int IR_RECEIVE_PIN = 4;

void setup() {
    Serial.begin(115200);
    IrReceiver.begin(IR_RECEIVE_PIN, ENABLE_LED_FEEDBACK); // Start the receiver, enable feedback LED, take LED feedback pin from the internal boards definition
    Serial.print(F("Ready to receive IR signals at pin "));
    Serial.println(IR_RECEIVE_PIN);
}

void loop() {
    if (IrReceiver.decode()) {
        Serial.println(IrReceiver.decodedIRData.decodedRawData);
        delay(100);
        IrReceiver.resume(); // Enable receiving of the next value               
    }
}