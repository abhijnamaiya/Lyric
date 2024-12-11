start

num x;
str s;
bool b;

play x 5;
play s "text";

bool play y yeah;

check (x > 4) here {
  release "greater";
  play x 3;
} there {
  release "greater";
}

check (x > 4) here {
  release "greater";
  play x 3;
} there {
  release "lesser";
}

stop