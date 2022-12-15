class Sensor{
  PVector pos;
  PVector beacon;
  int dist;
  
  Sensor(PVector p, PVector b) {
    pos = p;
    beacon = b;
    dist = int(abs(b.x-p.x) + abs(b.y-p.y));
  } 
}


Sensor[] sensors = {
  new Sensor(new PVector(3088287, 2966967), new PVector(3340990, 2451747)),
  new Sensor(new PVector(289570, 339999), new PVector(20077, 1235084)),
  new Sensor(new PVector(1940197, 3386754), new PVector(2010485, 3291030)),
  new Sensor(new PVector(1979355, 2150711), new PVector(1690952, 2000000)),
  new Sensor(new PVector(2859415, 1555438), new PVector(3340990, 2451747)),
  new Sensor(new PVector(1015582, 2054755), new PVector(1690952, 2000000)),
  new Sensor(new PVector(1794782, 3963737), new PVector(2183727, 4148084)),
  new Sensor(new PVector(2357608, 2559811), new PVector(2010485, 3291030)),
  new Sensor(new PVector(2936, 1218210), new PVector(20077, 1235084)),
  new Sensor(new PVector(2404143, 3161036), new PVector(2010485, 3291030)),
  new Sensor(new PVector(12522, 1706324), new PVector(20077, 1235084)),
  new Sensor(new PVector(1989162, 3317864), new PVector(2010485, 3291030)),
  new Sensor(new PVector(167388, 3570975), new PVector(-1018858, 4296788)),
  new Sensor(new PVector(1586527, 2233885), new PVector(1690952, 2000000)),
  new Sensor(new PVector(746571, 1442967), new PVector(20077, 1235084)),
  new Sensor(new PVector(3969726, 3857699), new PVector(3207147, 4217920)),
  new Sensor(new PVector(1403393, 2413121), new PVector(1690952, 2000000)),
  new Sensor(new PVector(2343717, 3649198), new PVector(2183727, 4148084)),
  new Sensor(new PVector(1473424, 688269), new PVector(2053598, 169389)),
  new Sensor(new PVector(2669347, 190833), new PVector(2053598, 169389)),
  new Sensor(new PVector(2973167, 3783783), new PVector(3207147, 4217920)),
  new Sensor(new PVector(2011835, 3314181), new PVector(2010485, 3291030)),
  new Sensor(new PVector(1602224, 2989728), new PVector(2010485, 3291030)),
  new Sensor(new PVector(3928889, 1064434), new PVector(3340990, 2451747)),
  new Sensor(new PVector(2018358, 3301778), new PVector(2010485, 3291030)),
  new Sensor(new PVector(1811905, 2084187), new PVector(1690952, 2000000)),
  new Sensor(new PVector(1767697, 1873118), new PVector(1690952, 2000000)),
  new Sensor(new PVector(260786, 1154525), new PVector(20077, 1235084)),
};

void setup(){
  colorMode(HSB);
  size(800, 800);
  strokeWeight(3000);
}

void draw(){
  scale(0.0002);
  background(0);
  stroke(0, 255, 255);
  for(int i = 0;i < sensors.length;i++){
    stroke(i * 255.0 / (float)sensors.length, 255, 255);
    Sensor sensor = sensors[i];
    line(sensor.pos.x, sensor.pos.y, sensor.beacon.x, sensor.beacon.y);
    
    line(sensor.pos.x + sensor.dist, sensor.pos.y, sensor.pos.x, sensor.pos.y + sensor.dist);
    line(sensor.pos.x, sensor.pos.y + sensor.dist, sensor.pos.x - sensor.dist, sensor.pos.y);
    line(sensor.pos.x - sensor.dist, sensor.pos.y, sensor.pos.x, sensor.pos.y - sensor.dist);
    line(sensor.pos.x, sensor.pos.y - sensor.dist, sensor.pos.x + sensor.dist, sensor.pos.y);
  }
}
