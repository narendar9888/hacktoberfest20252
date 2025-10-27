lil diff = a ^ b;
for (int i = 0; i < 64; ++i) {
    if (diff & (1LL << i)) ans.push_back(1LL << i);
}
