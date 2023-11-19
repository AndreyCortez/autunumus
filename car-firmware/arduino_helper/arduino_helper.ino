#include <MsTimer2.h>
#include <SPI.h>
#include <mcp2515.h>
#include <math.h>

struct can_frame canMsg;
MCP2515 mcp2515(10);

#define motor_esquerdo_pwm 9
#define motor_esquerdo_in1 7
#define motor_esquerdo_in2 8

#define motor_direito_pwm 6
#define motor_direito_in3 3
#define motor_direito_in4 4

#define tensao_entrada 12.0
#define tensao_maxima_motor 8.0
#define divisor_tensao tensao_maxima_motor / tensao_entrada

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

#define TAM_FILTRO_MM 3
#define TEMPO_AMOSTRAGEM_VELOCIDADE 1000

uint16_t ultimos_resultados[TAM_FILTRO_MM] = {0, 0, 0};
uint8_t ind_ultimos_resultados = 0;
uint32_t tempo_inicio = 0;

const float tempo_seg = (float)TEMPO_AMOSTRAGEM_VELOCIDADE / 1000;

void amostragem_velocidade()
{
    Serial.println((float)TCNT1 / (tempo_seg));
    TCNT1 = 0;
}

int overflow_count = 0;

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

    TCCR1A = 0;          // Init Timer1A
    TCCR1B = 0;          // Init Timer1B
    TCCR1B |= B00000111; // External Clock on T1 Pin (RISING)
    TCNT1 = 0;

    // Gambiarra pra conseguir um 5V extra heheheheh
    pinMode(A0, OUTPUT);
    digitalWrite(A0, HIGH);

    MsTimer2::set(TEMPO_AMOSTRAGEM_VELOCIDADE, amostragem_velocidade); // 500ms period
    MsTimer2::start();
}

void loop()
{

    // Serial.println(TCNT1);

    // if (digitalRead(9))
    // {
    //     Serial.println("sla");
    // }

    if (mcp2515.readMessage(&canMsg) == MCP2515::ERROR_OK)
    {

        // debug_messages(canMsg);

        if (canMsg.can_id == 2 && canMsg.can_dlc == 6)
        {
            // Serial.println("Setando potencia pros motores");
            analogWrite(motor_esquerdo_pwm, canMsg.data[0] * divisor_tensao);
            digitalWrite(motor_esquerdo_in1, canMsg.data[1]);
            digitalWrite(motor_esquerdo_in2, canMsg.data[2]);

            analogWrite(motor_direito_pwm, canMsg.data[3] * divisor_tensao);
            digitalWrite(motor_direito_in3, canMsg.data[4]);
            digitalWrite(motor_direito_in4, canMsg.data[5]);
        }
    }
}