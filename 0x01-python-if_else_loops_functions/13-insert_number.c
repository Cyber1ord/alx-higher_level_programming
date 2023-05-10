#include "lists.h"

/**
 * insert_node - inserts a new node at a given position
 * @head: pointer to a pointer to the head of the linked list
 * @number: value to be added to the new node
 *
 * Return: address of the new node, or NULL if it fails
 */
listint_t *insert_node(listint_t **head, int number)
{
	listint_t *new_node, *current_node, *prev_node = NULL;

	new_node = malloc(sizeof(listint_t));
	if (new_node == NULL)
		return (NULL);

	new_node->n = number;
	new_node->next = NULL;

	if (*head == NULL)
	{
		*head = new_node;
		return (new_node);
	}

	current_node = *head;

	while (current_node != NULL && current_node->n < number)
	{
		prev_node = current_node;
		current_node = current_node->next;
	}

	if (prev_node == NULL)
	{
		new_node->next = *head;
		*head = new_node;
	}
	else
	{
		new_node->next = prev_node->next;
		prev_node->next = new_node;
	}

	return (new_node);
}

