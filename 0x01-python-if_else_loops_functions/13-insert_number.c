#include "lists.h"
/**
 * insert_node - insert a node into list
 * @head: pointer to the list
 * @number: int value of new node
 * Return: Success: address of new node
 * Fail: NULL
 */

listint_t *insert_node(listint_t **head, int number)
{
	listint_t *curr, *prev = NULL, *new;

	if (head == NULL)
		return (NULL);
	new = malloc(sizeof(listint_t));
	if (new == NULL)
		return (NULL);
	new->n = number;
	new->next = NULL;

	if (*head == NULL || (*head)->n > number)
	{
		new->next = *head;
		*head = new;
		return (new);
	}
	for (curr = *head; curr != NULL && curr->n < number; curr = curr->next)
		prev = curr;
	new->next = prev->next;
	prev->next = new;
	return (new);
}
