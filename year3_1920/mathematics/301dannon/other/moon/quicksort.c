#include <stdio.h>
#include <string.h>
#include <stdlib.h>
typedef struct number* numLink;

typedef struct number {
	numLink left;
	numLink right;
	double digit;
} number;

void bigRight(number* std, number* link);
void smallLeft(number* std, number* link);

int main() {
	FILE *file_pointer;
	number *(input[1000]);
	
	char string[100];
	char ch;
	int count = 0;
	file_pointer = fopen("../list", "r");
	fscanf(file_pointer, "%[^\n]s", string);
	char *temp = strtok(string, " ");

	while (temp != NULL) {
		input[count] = malloc(sizeof(number));
		input[count]->digit = atof(temp);
		//여기에 이어보기
		if (count == 0) {
			input[count]->left = NULL;
		}
		else {
			input[count - 1]->right = input[count];
			input[count]->left = input[count-1];
		}
		temp = strtok(NULL, " ");
		count++;
		//여기에 모두를 이어보기
	}
	printf("count is %d\n", count);

	// input[count-1]->right = NULL;
	// numLink head;
	// head= input[0];
	// while (head != NULL) {
	// 	printf("%lf%\n", head->digit);
	// 	head = head->right;
	// }
	// //count 가 4니까 4 가지고 놀아보기
	// for (int i = 0;i < 4;i++) {
	// 	//왼쪽 탐색
	// 	numLink head = input[i];
	// 	numLink temp = head;
	// 	while (temp->left!=NULL) {
	// 		if (head->digit < temp->digit)
	// 			bigRight(head, temp);
	// 		temp = temp->left;
	// 	}
	// 	head = input[i];
	// 	temp = head;
	// 	//오른쪽 탐색
	// 	while (temp!=NULL) {
	// 		if (head->digit > temp->digit)
	// 			smallLeft(head, temp);
	// 		temp = temp->right;
	// 	}
	// }
	// numLink first = input[count - 1];
	// while (first->left != NULL)
	// 	first = first->left;
	// printf("result is ");
	// while (first->right != NULL) {
	// 	printf("%lf   ", first->digit);
	// 	first = first->right;
	// }

	// printf("%lf", first->digit);

	return 0;
}

void bigRight(number* std, number* link) {
	//std에 기준을 받고, link가 더 큰 digit을 가질 때 발동하는 함수
	numLink temp1;
	numLink temp2;
	if (std->right == NULL) {
		if (link->left == NULL) {
			(link->right)->left = NULL;
		}
		else {
			(link->right)->left = link->left;
			(link->left)->right = link->right;
		}
		//std 기준
		std->right = link;
		link->right = NULL;
		link->left = std;

	}
	if (link->left == NULL) { //link가 가장 왼쪽에 있는 경우
		(link->right)->left = NULL; //그 뒤에거를 맨앞으로 보내기
		temp1 = std->right;
		std->right = link;
		link->right = temp1;
		temp1->left = link;
		link->left = std;
	}
	else { //link가 가장 왼쪽에 있지 않은 경우
		(link->right)->left = link->left;
		(link->left)->right = link->right;
		temp1 = std->right;
		std->right = link;
		link->right = temp1;
		temp1->left = link;
		link->left = std;
	}
}
void smallLeft(number* std, number* link) {
	numLink temp;
	if (std->left == NULL) {
		//link 가 맨 오른쪽일 때
		if (link->right == NULL) {
			(link->left)->right = NULL;
		}
		else {
			(link->right)->left = link->left;
			(link->left)->right = link->right;
		}

		// std 기준
		std->left = link;
		link->left = NULL;
		link->right = std;
	}

	else if (link->right == NULL) {
		(link->left)->right = NULL; //그 전 친구 맨 오른쪽 취급
		temp = std->left;
		temp->right = link;
		link->left = temp;
		std->left = link;
		link->right = std;
	}
	else { //link가 가장 오른쪽에 있지 않은 경우
		(link->left)->right = link->right;
		(link->right)->left = link->left;
		temp = std->left;
		temp->right = link;
		link->left = temp;
		std->left = link;
		link->right = std;
	}
}