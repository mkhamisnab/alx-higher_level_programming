#ifndef LISTS_H
#define LISTS_H

#include <stdio.h>
#include <stdlib.h>

/**
 * struct listint_s - singly linked list
 * @n: integer
 * @next: points to the next node
 *
 * Description: Definition of a singly linked list node structure
 */
typedef struct listint_s
{
    int n;
    struct listint_s *next;
} listint_t;

/**
 * print_listint - Prints all the elements of a linked list.
 * @h: Pointer to the head node of the list.
 * Return: The number of nodes in the list.
 */
size_t print_listint(const listint_t *h);

/**
 * add_nodeint_end - Adds a new node at the end of a linked list.
 * @head: Pointer to the head pointer of the list.
 * @n: The value to be stored in the new node.
 * Return: Pointer to the newly added node.
 */
listint_t *add_nodeint_end(listint_t **head, const int n);

/**
 * free_listint - Frees a linked list.
 * @head: Pointer to the head node of the list.
 */
void free_listint(listint_t *head);

/**
 * is_palindrome - Checks if a linked list is a palindrome.
 * @head: Pointer to the head pointer of the list.
 * Return: 1 if the list is a palindrome, 0 otherwise.
 */
int is_palindrome(listint_t **head);

#endif /* LISTS_H */
