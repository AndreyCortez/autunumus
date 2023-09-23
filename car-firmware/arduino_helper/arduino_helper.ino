#include <SPI.h>
#include <mcp2515.h>
#include <math.h>

struct can_frame canMsg;
MCP2515 mcp2515(10);

#define motor_esquerdo_pwm 6
#define motor_esquerdo_in1 A0
#define motor_esquerdo_in2 A1

#define motor_direito_pwm 5
#define motor_direito_in3 A2
#define motor_direito_in4 A3

void debug_messages(can_frame msg)
{
    Serial.print(msg.can_id, HEX); // print ID
    Serial.print(" ");
    Serial.print(msg.can_dlc, HEX); // print DLC
    Serial.print(" ");

    for (int i = 0; i < msg.can_dlc; i++)
    { // print the data
        Serial.print(msg.data[i], HEX);
        Serial.print(" ");
    }

    Serial.println();
}

void setup()
{
    Serial.begin(9600);

    mcp2515.reset();
    mcp2515.setBitrate(CAN_500KBPS);
    mcp2515.setNormalMode();

    Serial.println("------- CAN Read ----------");
    Serial.println("ID  DLC   DATA");

    pinMode(motor_esquerdo_pwm, OUTPUT);
    pinMode(motor_esquerdo_in1, OUTPUT);
    pinMode(motor_esquerdo_in2, OUTPUT);
    pinMode(motor_direito_pwm, OUTPUT);
    pinMode(motor_direito_in3, OUTPUT);
    pinMode(motor_direito_in4, OUTPUT);

    digitalWrite(motor_esquerdo_in1, LOW);
    digitalWrite(motor_esquerdo_in2, HIGH);
    digitalWrite(motor_direito_in3, LOW);
    digitalWrite(motor_direito_in4, HIGH);
}

void loop()
{

    if (mcp2515.readMessage(&canMsg) == MCP2515::ERROR_OK)
    {

        debug_messages(canMsg);

        if (canMsg.can_id == 2 && canMsg.can_dlc == 2)
        {
            analogWrite(motor_esquerdo_pwm, canMsg.data[0]);
            analogWrite(motor_esquerdo_pwm, abs(canMsg.data[1] - 127) * 2);
            digitalWrite(motor_direito_in3, canMsg.data[1] > 127);
            digitalWrite(motor_direito_in4, canMsg.data[1] < 127);
        }
    }
}
