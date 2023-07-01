
R = 0.1;
H = 1.0;
L = 6.0;
Nr = 24;
Nh = 16;
Nl = 64;

// Centro do cilindro
c[] = {H/2, H/2, 0};

//+
Point(1) = {0.0, 0.0, 0, 1.0};
//+
Point(2) = {  H, 0.0, 0, 1.0};
//+
Point(3) = {  L, 0.0, 0, 1.0};
//+
Point(4) = {  L,   H, 0, 1.0};
//+
Point(5) = {  H,   H, 0, 1.0};
//+
Point(6) = {0.0,   H, 0, 1.0};
//+
Point(7) = {c[0]-R, c[1], 0, 1.0};
//+
Point(8) = {c[0], c[1]-R, 0, 1.0};
//+
Point(9) = {c[0]+R, c[1], 0, 1.0};
//+
Point(10) = {c[0], c[1]+R, 0, 1.0};
//+
Point(11) = {c[0], c[1], 0, 1.0};
//+
Rotate {{0, 0, 1}, {c[0], c[1], 0}, -Pi/4} {
  Point{7}; Point{8}; Point{9}; Point{10}; 
}
//+
Line(1) = {1, 2};
//+
Line(2) = {2, 3};
//+
Line(3) = {3, 4};
//+
Line(4) = {4, 5};
//+
Line(5) = {5, 6};
//+
Line(6) = {6, 1};
//+
Line(7) = {2, 5};
//+
Line(8) = {10, 5};
//+
Line(9) = {7, 6};
//+
Line(10) = {8, 1};
//+
Line(11) = {9, 2};
//+
Circle(12) = {10, 11, 7};
//+
Circle(13) = {7, 11, 8};
//+
Circle(14) = {8, 11, 9};
//+
Circle(15) = {9, 11, 10};
//+
Transfinite Curve {13, 6, 5, 12, 14, 1, 7, 15, 3} = Nh Using Progression 1;
//+
Transfinite Curve {9, 10, 8, 11} = Nr Using Progression 1.1;
//+
Transfinite Curve {4, 2} = Nl Using Progression 1;
//+
Curve Loop(1) = {12, 9, -5, -8};
//+
Plane Surface(1) = {1};
//+
Curve Loop(2) = {9, 6, -10, -13};
//+
Plane Surface(2) = {2};
//+
Curve Loop(3) = {10, 1, -11, -14};
//+
Plane Surface(3) = {3};
//+
Curve Loop(4) = {8, -7, -11, 15};
//+
Plane Surface(4) = {4};
//+
Curve Loop(5) = {4, -7, 2, 3};
//+
Plane Surface(5) = {5};
//+
Transfinite Surface {1};
//+
Transfinite Surface {2};
//+
Transfinite Surface {3};
//+
Transfinite Surface {4};
//+
Transfinite Surface {5};
//+
Extrude {0, 0, 0.05} {
  Surface{1}; Surface{2}; Surface{3}; Surface{4}; Surface{5}; Curve{4}; Curve{7}; Curve{2}; Curve{3}; Curve{8}; Curve{5}; Curve{9}; Curve{12}; Curve{6}; Curve{10}; Curve{13}; Curve{1}; Curve{14}; Curve{11}; Curve{15}; Layers {1}; Recombine;
}
//+
Physical Surface("simetria", 126) = {37, 2, 59, 103, 4, 1, 3, 81, 125, 5};
//+
Physical Surface("inlet", 127) = {50};
//+
Physical Surface("outlet", 128) = {124};
//+
Physical Surface("parede", 129) = {32, 112, 72, 120};
//+
Physical Surface("cilindro", 130) = {24, 58, 80, 102};
//+
Physical Volume("Volume", 131) = {1, 2, 3, 4, 5};
