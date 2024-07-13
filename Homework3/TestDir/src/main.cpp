/*******************************************************************
    A telegram bot for your ESP8266 that responds
    with whatever message you send it.

    Parts:
    D1 Mini ESP8266 * - http://s.click.aliexpress.com/e/uzFUnIe
    (or any ESP8266 board)

      = Affilate

    If you find what I do useful and would like to support me,
    please consider becoming a sponsor on Github
    https://github.com/sponsors/witnessmenow/


    Written by Brian Lough
    YouTube: https://www.youtube.com/brianlough
    Tindie: https://www.tindie.com/stores/brianlough/
    Twitter: https://twitter.com/witnessmenow
 *******************************************************************/

// #include <ESP8266WiFi.h>
// IPAddress ip(192, 168, 1, 184); // змініть на IP, який підходить для вашої мережі
// IPAddress gateway(192, 168, 1, 1);
// IPAddress subnet(255, 255, 255, 0);
// const char* ssid = "Voblaco_home";
// const char* password = "White_2023";
// void setup() {
//   Serial.begin(115200);
//   WiFi.config(ip, gateway, subnet);
//   WiFi.begin(ssid, password);

//   int attempts = 0;
//   while (WiFi.status() != WL_CONNECTED && attempts < 20) {
//     delay(500);
//     Serial.print(".");
//     attempts++;
//   }

//   if (WiFi.status() == WL_CONNECTED) {
//     Serial.println("Connected to WiFi");
//   } else {
//     Serial.println("Failed to connect to WiFi");
//   }
// }

// void loop() {}


#include <Arduino.h>
#include <WiFiManager.h>
#include <UniversalTelegramBot.h>
#include "sensitive.h"

int button = 4;
int electricityState=0;
int electricityStateBefore = 0;
const unsigned long BOT_MTBS = 1000; // mean time between scan messages
unsigned long bot_lasttime; // last time messages' scan has been done

WiFiManager wm;
WiFiClientSecure secured_client;
UniversalTelegramBot bot(BOT_TOKEN, secured_client);
X509List cert(TELEGRAM_CERTIFICATE_ROOT);

void setDefaultLed(bool isOn);
void blinkDefaultLed();
void processTgMessages();
void handleNewMessages(int numNewMessages);

void setup() {
  Serial.begin(115200);
  pinMode(button, INPUT);
  
  secured_client.setTrustAnchors(&cert);
  // secured_client.setCACert(TELEGRAM_CERTIFICATE_ROOT);

  wm.setSTAStaticIPConfig(IPAddress(192,168,50,2), IPAddress(192, 168, 1, 1), IPAddress(255,255,255,0));
  wm.setShowStaticFields(false);
  wm.setShowDnsFields(false);
  wm.setDebugOutput(3);
  wm.setSaveConnectTimeout(300); // it is incredibly large number, but if you are far away from WIFI router - it will help you
  wm.setConnectTimeout(300);

  // Automatically connect using saved credentials,
  // if connection fails, it starts an access point with the specified name ( "AutoConnectAP"),
  // if empty will auto generate SSID, if password is blank it will be anonymous AP (wm.autoConnect())
  // then goes into a blocking loop awaiting configuration and will return success result
  pinMode(LED_BUILTIN, OUTPUT);
  blinkDefaultLed();

  setDefaultLed(true);
  if(wm.autoConnect("Voblaco_ligh_bot","password")) {
      Serial.println("Failed to connect");
      // ESP.restart();
  } 
  else {
      //if you get here you have connected to the WiFi    
      Serial.println("connected...yeey :)");
  }  

  bot.waitForResponse = 2500;

  Serial.println("[me] CONNECTED");
  setDefaultLed(false);
  Serial.println("[me] SHOT DOWN LED");
  Serial.println("[me] SET SERTIFICATE");
  //bot.sendMessage("-811306935", "Bot started!");
  Serial.println("[me] SEND MESSAGE");
}

void loop() {
  blinkDefaultLed();
  processTgMessages();

  electricityState=digitalRead(button);
  if (electricityState != electricityStateBefore) {
    if (electricityState == 1) {
      Serial.print("\rOFF ");
      delay(200);
    }
    if (electricityState==0) {
      Serial.print("\rON ");
      delay(200);
    }
  }
  
}

void setDefaultLed(bool isOn) {
  if (isOn) {
    analogWrite(LED_BUILTIN, 0);
  } else {
    analogWrite(LED_BUILTIN, 0);
  }
}

void blinkDefaultLed() {
  for(int dutyCycle = 255; dutyCycle > 0; dutyCycle--){
    // changing the LED brightness with PWM
    analogWrite(LED_BUILTIN, dutyCycle);
    delay(3);
  }
  for(int dutyCycle = 0; dutyCycle < 255; dutyCycle++){   
    // changing the LED brightness with PWM
    analogWrite(LED_BUILTIN, dutyCycle);
    delay(3);
  }
  delay(2000);
}

void processTgMessages() {
  Serial.println("processing messages");
  if (millis() - bot_lasttime > BOT_MTBS)
  {
    Serial.println("Checking updates");
    bot.sendMessage("294086745", "Hi!", "");
    int numNewMessages = bot.getUpdates(bot.last_message_received + 1);
    Serial.print("Message count: ");
    Serial.println(numNewMessages);

    while (numNewMessages)
    {
      Serial.println("got response");
      handleNewMessages(numNewMessages);
      numNewMessages = bot.getUpdates(bot.last_message_received + 1);
    }

    bot_lasttime = millis();
  }
}

void handleNewMessages(int numNewMessages)
{
  for (int i = 0; i < numNewMessages; i++)
  {
    String space = " ";
    bot.sendMessage(bot.messages[i].chat_id, bot.messages[i].text + space + bot.messages[i].chat_id, "");
  }
}