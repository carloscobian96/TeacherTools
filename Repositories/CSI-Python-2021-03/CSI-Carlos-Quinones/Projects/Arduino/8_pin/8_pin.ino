int x;
void setup() {
 Serial.begin(115200);
 Serial.setTimeout(1);
}
void loop() {
 while (!Serial.available());
 x = Serial.readString().toInt();
 //Serial.print(x);

 if (x ==1){
  digitalWrite(1, LOW);
  digitalWrite(2, LOW);
  digitalWrite(3, LOW);
  digitalWrite(4, LOW);
  digitalWrite(5, LOW);
  digitalWrite(6, LOW);
  digitalWrite(7, LOW);
  digitalWrite(8, LOW);
  digitalWrite(9, LOW);
  digitalWrite(10, LOW);
  
  digitalWrite(9, HIGH);
 digitalWrite(1, HIGH);
 }
 if (x ==2){
  digitalWrite(1, LOW);
  digitalWrite(2, LOW);
  digitalWrite(3, LOW);
  digitalWrite(4, LOW);
  digitalWrite(5, LOW);
  digitalWrite(6, LOW);
  digitalWrite(7, LOW);
  digitalWrite(8, LOW);
  digitalWrite(9, LOW);
  digitalWrite(10, LOW);
  digitalWrite(7, HIGH);
 digitalWrite(6, HIGH);
  digitalWrite(10, HIGH);
 digitalWrite(1, HIGH);
  digitalWrite(2, HIGH);
 }
 if (x ==3){
  digitalWrite(1, LOW);
  digitalWrite(2, LOW);
  digitalWrite(3, LOW);
  digitalWrite(4, LOW);
  digitalWrite(5, LOW);
  digitalWrite(6, LOW);
  digitalWrite(7, LOW);
  digitalWrite(8, LOW);
  digitalWrite(9, LOW);
  digitalWrite(10, LOW);
  digitalWrite(7, HIGH);
 digitalWrite(6, HIGH);
  digitalWrite(10, HIGH);
   digitalWrite(4, HIGH);
    digitalWrite(2, HIGH);
 }
 if (x ==4){
  digitalWrite(1, LOW);
  digitalWrite(2, LOW);
  digitalWrite(3, LOW);
  digitalWrite(4, LOW);
  digitalWrite(5, LOW);
  digitalWrite(6, LOW);
  digitalWrite(7, LOW);
  digitalWrite(8, LOW);
  digitalWrite(9, LOW);
  digitalWrite(10, LOW);
  digitalWrite(9, HIGH);
 digitalWrite(6, HIGH);
  digitalWrite(10, HIGH);
   digitalWrite(4, HIGH);
 }
 if (x ==5){
  digitalWrite(1, LOW);
  digitalWrite(2, LOW);
  digitalWrite(3, LOW);
  digitalWrite(4, LOW);
  digitalWrite(5, LOW);
  digitalWrite(6, LOW);
  digitalWrite(7, LOW);
  digitalWrite(8, LOW);
  digitalWrite(9, LOW);
  digitalWrite(10, LOW);
  digitalWrite(7, HIGH);
 digitalWrite(9, HIGH);
  digitalWrite(10, HIGH);
   digitalWrite(4, HIGH);
    digitalWrite(2, HIGH);
 }
 if (x ==6){
  digitalWrite(1, LOW);
  digitalWrite(2, LOW);
  digitalWrite(3, LOW);
  digitalWrite(4, LOW);
  digitalWrite(5, LOW);
  digitalWrite(6, LOW);
  digitalWrite(7, LOW);
  digitalWrite(8, LOW);
  digitalWrite(9, LOW);
  digitalWrite(10, LOW);
  digitalWrite(9 , HIGH);
 digitalWrite(10, HIGH);
  digitalWrite(7, HIGH);
   digitalWrite(4, HIGH);
    digitalWrite(2, HIGH);
     digitalWrite(1, HIGH);
 }
 if (x ==7){
  digitalWrite(1, LOW);
  digitalWrite(2, LOW);
  digitalWrite(3, LOW);
  digitalWrite(4, LOW);
  digitalWrite(5, LOW);
  digitalWrite(6, LOW);
  digitalWrite(7, LOW);
  digitalWrite(8, LOW);
  digitalWrite(9, LOW);
  digitalWrite(10, LOW);
  digitalWrite(7, HIGH);
 digitalWrite(6, HIGH);
  digitalWrite(4, HIGH);
 }
 if (x ==8){
  digitalWrite(1, LOW);
  digitalWrite(2, LOW);
  digitalWrite(3, LOW);
  digitalWrite(4, LOW);
  digitalWrite(5, LOW);
  digitalWrite(6, LOW);
  digitalWrite(7, LOW);
  digitalWrite(8, LOW);
  digitalWrite(9, LOW);
  digitalWrite(10, LOW);
 digitalWrite(7, HIGH);
 digitalWrite(6, HIGH);
  digitalWrite(4, HIGH);
   digitalWrite(2, HIGH);
    digitalWrite(1, HIGH);
     digitalWrite(9, HIGH);
      digitalWrite(10, HIGH);
     
 }
 if (x ==9){
  digitalWrite(1, LOW);
  digitalWrite(2, LOW);
  digitalWrite(3, LOW);
  digitalWrite(4, LOW);
  digitalWrite(5, LOW);
  digitalWrite(6, LOW);
  digitalWrite(7, LOW);
  digitalWrite(8, LOW);
  digitalWrite(9, LOW);
  digitalWrite(10, LOW);
  digitalWrite(7, HIGH);
 digitalWrite(6, HIGH);
  digitalWrite(10, HIGH);
   digitalWrite(9, HIGH);
    digitalWrite(4, HIGH);
 }
 
 

 
 }

 


 
