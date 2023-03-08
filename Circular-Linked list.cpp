
#include <iostream>

using namespace std;

//single linked list attributes
struct node{
    int data;
    node *next;
};

//Global variables
struct node *head = new node; // allocating memory for head
struct node *nodePtr = head; // pointer for traversing list

//function for inserting node and data
void newNode (int n, int length){
    nodePtr->next = new node; //allocating memory for next node(s)
        nodePtr->next->data= n+1; //value inside node
        nodePtr = nodePtr->next;

        //reset to head if iteration in the list is finished
        if (n==length-1){
            nodePtr->next=head;
            nodePtr=head;
        }
}

//function for printing data
void displayVal (){
      cout<<nodePtr->data<<" ("<<&nodePtr->data<<")"<<endl;
      nodePtr = nodePtr->next;
}

//function for deleting nodes
void deleteNode (){
        head = nodePtr->next;
        delete nodePtr;
        nodePtr = head;
}

int main()
{

    int nodeLength = 20; int displayLength = 40;
    head->data=1;

    //loop for allocating memory and assigning value
    for (int i=head->data; i<nodeLength; i++){
        newNode (i,nodeLength);
    }

    // printing data
    for (int j=0; j<displayLength; j++){
    displayVal ();
    }

    //iterating and deleting nodes
    for (int k=0; k<nodeLength; k++){
       deleteNode ();
    }

    //resetting pointers to avoid garbage values
    delete head;
    head = (nullptr);
    nodePtr = {nullptr};


    return 0;
}
