#include "lists.h"

/**
 * reverse_listint - reverses a linked list.
 * @head: pointer to the first node.
 *
 * Return: the pointer (head).
 */

void reverse_listint(listint_t **head)
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
 * is_palindrome - checks if a linked list is a palindrome.
 * @head: double pointer.
 *
 * Return: 1 if successful, if not return 0.
 */

int is_palindrome(listint_t **head)
{
    if (*head == NULL || (*head)->next == NULL)
        return (1);

    listint_t *slow = *head;
    listint_t *fast = *head;
    listint_t *temp = *head;
    listint_t *dup = NULL;

    while (fast != NULL && fast->next != NULL)
    {
        slow = slow->next;
        fast = fast->next->next;
    }

    if (fast != NULL)
    {
        dup = slow->next;
    }
    else
    {
        dup = slow;
    }

    reverse_listint(&dup);

    while (dup != NULL && temp != NULL)
    {
        if (temp->n != dup->n)
            return (0);

        temp = temp->next;
        dup = dup->next;
    }

    return (1);
}
