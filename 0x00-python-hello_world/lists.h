#ifndef LISTS_H
#define LISTS_H

#include <stddef.h>

typedef struct listint_s
{
    int n;
    struct listint_s *next;
} listint_t;

int check_cycle(listint_t *list);

#endif /* LISTS_H */
