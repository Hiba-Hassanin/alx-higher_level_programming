#include "lists.h"


/**

 * is_palindrome - checks if a singly linked list is a palindrome.
 * @head: the head.
 *
 * Return: 1 if the list is a palindrome.
 */

int is_palindrome(listint_t *head)
{
    if (head == NULL)
        return (0);

    listint_t *slow_ptr = head;
    listint_t *fast_ptr = head;
    listint_t *prev_slow_ptr = NULL;
    listint_t *mid_ptr = NULL;
    listint_t *second_half = NULL;
    int is_palindrome = 1;

    while (fast_ptr != NULL && fast_ptr->next != NULL)
    {
        fast_ptr = fast_ptr->next->next;
        prev_slow_ptr = slow_ptr;
        slow_ptr = slow_ptr->next;
    }

    if (fast_ptr != NULL)
    {
        mid_ptr = slow_ptr;
        slow_ptr = slow_ptr->next;
    }

    second_half = slow_ptr;
    prev_slow_ptr->next = NULL;
    reverse_list(&second_half);

    is_palindrome = compare_lists(head, second_half);

    reverse_list(&second_half);

    if (mid_ptr != NULL)
    {
        prev_slow_ptr->next = mid_ptr;
        mid_ptr->next = second_half;
    }
    else
    {
        prev_slow_ptr->next = second_half;
    }

    return (is_palindrome);
}

/**
 * reverse_list - reverses the list.
 * @head: pointer to the head.
 */

void reverse_list(listint_t **head)
{
    listint_t *prev = NULL;
    listint_t *current = *head;
    listint_t *next = NULL;

    while (current != NULL)
    {
        next = current->next;
        current->next = prev;
        prev = current;
        current = next;
    }

    *head = prev;
}

/**
 * compare_lists - compares two of the linked lists.
 * @head1: pointer to the head of the first one.
 * @head2: pointer to the head of the second one.
 *
 * Return: 1 if the lists are identical, if not return 0.
 */

int compare_lists(listint_t *head1, listint_t *head2)
{
    while (head1 != NULL && head2 != NULL)
    {
        if (head1->n != head2->n)
            return (0);

        head1 = head1->next;
        head2 = head2->next;
    }

    if (head1 == NULL && head2 == NULL)
        return (1);

    return (0);
}
