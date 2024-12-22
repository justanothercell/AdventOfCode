#include <inttypes.h>
#include <stdio.h>
#include <stdlib.h>

static inline uint64_t mix(uint64_t result, uint64_t number) {
    return result ^ number;
}

static inline uint64_t prune(uint64_t result) {
    return result % 16777216;
}

static inline uint64_t next(uint64_t number) {
    number = prune(mix(number * 64, number));
    number = prune(mix(number / 32, number));
    number = prune(mix(number * 2048, number));
    return number;
}


int main() {
    // 2<<19 reserves space for all 2**20 possibel values, no compacting needed
    // map window -> total babanas; zeroed out with calloc
    uint64_t* map = calloc(2 << 19, sizeof(uint64_t));
    // set keeping track which window was already encountered this time; zeroed out with calloc
    size_t* mask = calloc(2 << 19, sizeof(size_t));

    uint64_t max_window = 0;
    uint64_t max_profit = 0;

    uint64_t* numbers = malloc(sizeof(uint64_t));
    size_t n_length = 0;
    size_t n_capacity = 1;

    FILE* infile = fopen("input.txt", "r");
    uint64_t number;
    while (fscanf(infile, "%"PRIu64, &number) != EOF) {
        if (n_length == n_capacity) {
            n_capacity *= 2;
            numbers = realloc(numbers, sizeof(uint64_t) * n_capacity);
        }
        numbers[n_length++] = number;
    }

    printf("read %zu input numbers\n", n_length);

    for (size_t i = 0;i < n_length;i++) {
        uint64_t n = numbers[i];
        uint64_t window = 0;
        for (size_t j = 0;j < 2000;j++) {
            uint64_t nn = next(n);
            int64_t delta = nn % 10 - n % 10;
            window <<= 5;
            window |= abs(delta) | (delta < 0 ? 0b10000 : 0b00000);
            window &= 0b11111111111111111111; // 5*4
            n = nn;
            if (j < 4) continue; // window not initially filled yet
            if (mask[window] != i+1) { // this window has not yet appeared for this input
                mask[window] = i+1; // set mask for this window for this input
                map[window] += nn % 10; // add bananas
                if (map[window] > max_profit) {
                    max_profit = map[window];
                    max_window = window;
                }
            }
        }
    }

    printf("maximum possible profit is %"PRIu32" bananas\n", max_profit);
    printf("using window %020b\n", max_window);
}
