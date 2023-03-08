 /*
CCC121 Laboratory Exercise No. 1
Due: November 20, 2022 (Sunday) at 11:55PM
*/

#include <iostream>
#include <assert.h>

using namespace std;

/*
The structure to be used for representing a doubly-linked link. This struct
declaration should not be modified in any way.
*/
template <class E>
struct DLink
{
    E theElement;
    DLink<E> *nextPtr;
    DLink<E> *prevPtr;


};

/*
Complete this implementation variant of the doubly-linked list. Use the same
convention as described in the slides. The DLink declaration to be used here is
just a struct and should not be modified in any way. All of the operations of
the original DLink class must be done in the methods of this class. Use
assertions to ensure the correct operation of this ADT. All memory allocations
should be checked with assertions and all discarded memory must be properly
deallocated.
*/
template <class E>
class DList
{
    DLink<E> *head;
    DLink<E> *tail;
    DLink<E> *curr;
    int cnt;


public:
    // Return the size of the list
    int length() const
    {
        return cnt;
    }

    // The constructor with initial list size
    DList(int size)
    {
        this();
    }

    // The default constructor
    DList()
    {
       //head initialization
        head = new DLink<E>; assert(head != NULL);
        head->prevPtr = nullptr;
        head->nextPtr = tail;

        //tail initialization
        tail = new DLink <E>; assert(tail != NULL);
        tail->nextPtr = nullptr;
        tail->prevPtr = head;

        curr = head;
        cnt = 0;


    }

    // The copy constructor
    DList(const DList &source)
    {
        //initializing all the data members for copying
        //head initialization
        head = new DLink<E>; assert(head != NULL);
        head->prevPtr = nullptr;
        head->nextPtr = tail;

        //tail initialization
        tail = new DLink <E>; assert(tail != NULL);
        tail->nextPtr = nullptr;
        tail->prevPtr = head;

        curr = head;
        cnt = 0;

        DLink<E> *temp = source.head;

        //return value if list is empty
        if (source.head -> nextPtr = source.tail) {
            return;
        }

        //copying contens for the list
        while (temp->nextPtr != source.tail)
        {
            append(temp->nextPtr->theElement); //using append to copy contents of the list
            if (temp == source.curr)
            {
                curr = tail->prevPtr;
                temp = temp->nextPtr;
            }
        }

        cnt = source.cnt;


}
    // The class destructor
    ~DList()
    {
        //case if list is empty
        if (head -> nextPtr == tail) {
            delete head;
            delete tail;

            return;

        //delete entire list
        } else {
            clear();
            delete head;
            delete tail;

            return;
        }

    }

    // Empty the list
    void clear()
    {

        curr = head;

        //iterating through the list for deletion
        while (head -> nextPtr != tail) {
            DLink<E> *temp = head -> nextPtr; //creating a pointer for iteration
            head -> nextPtr = temp -> nextPtr;
            temp -> nextPtr -> prevPtr = head; // maintaining link of list
            delete temp;
        }

        //resetting the list and linking head and tail
        head->prevPtr = nullptr;
        head->nextPtr = tail;

        tail->nextPtr = nullptr;
        tail->prevPtr = head;

        curr = head;
        cnt = 0;




    }


    // Set current to first element
    void moveToStart()
    {
        curr = head;

    }

    // Set current element to end of list
    void moveToEnd()
    {
        curr = tail->prevPtr;


    }

    // Advance current to the next element
    void next()
    {
        curr = curr -> nextPtr;

    }

    // Return the current element
    E & getValue() const
    {
        return curr->nextPtr->theElement;
    }

    // Insert value at current position
    void insert(const E &it)
    {

        DLink<E> *newLink = new DLink<E>; assert(newLink != NULL);
        newLink->theElement = it;

        //inserting newlink and linking nodes
        newLink -> nextPtr = curr -> nextPtr;
        curr = newLink;
        newLink -> prevPtr = curr;
        curr -> nextPtr = newLink;
        cnt++;

    }


    // Append value at the end of the list
    void append(const E &it)
    {

        DLink<E> *newLink = new DLink<E>; assert(newLink != NULL); // allocating memory for append node
        newLink->theElement = it; //assigning value

        //linking nodes
        newLink -> nextPtr = tail;
        newLink -> prevPtr = tail -> prevPtr;
        tail -> prevPtr -> nextPtr = newLink;
        tail -> prevPtr = newLink;
        cnt++;


    }

    // Remove and return the current element
    E remove()
    {
        //setting value
        int removedElement = curr->theElement;

        DLink<E>* temp = curr->nextPtr; // Remember link

        //removing nodes from list
        curr->nextPtr->nextPtr->prevPtr = curr;
        curr->nextPtr = curr->nextPtr->nextPtr;

        delete temp; // Reclaim space
        cnt--; // Decrement cnt
        return removedElement;

    }

    // Advance current to the previous element
    void prev()
    {
        curr = curr->prevPtr;

    }

    // Return position of the current element
    int currPos() const
    {
        int currPos = 1;
        DLink<E> *current;

        //iterating to return to current element
        for (current = head -> nextPtr; current != curr; current = current -> nextPtr) {
            currPos++;
        }

        return currPos;

    }

    // Set current to the element at the given position
    void moveToPos(int pos)
    {
        //resseting curr
        curr = head;

       //iterating to the given position
        for (int i = 0; i<pos; i++){
            curr = curr->nextPtr;
        }

    }
};

/*
This is the main function for testing the implementation of the DList class.
This function can be freely modified.
*/
int main(void)
{
    int i;
    DList<int> theList;

    // populate the list
    for (i = 0; i < 10; ++i)
    {
        theList.append(i);
    }
    while (i < 20)
    {
        theList.insert(i);

        ++i;
    }

    // display the contents of the list
    theList.moveToStart();
    for (i = 0; i < theList.length(); ++i)
    {
        cout << theList.getValue() << " ";

        theList.next();
    }

    cout << "\n";

    // display the contents of the list in reverse order
    theList.moveToEnd();
    for (i = 0; i < theList.length(); ++i)
    {
        theList.prev();

        cout << theList.getValue() << " ";
    }
    cout << "\n";

    // replace the contents of the list

    theList.clear();

    for (i = 0; i < 10; ++i)
    {
        theList.append(i + 100);
    }

    // display the contents of the list
    theList.moveToStart();
    for (i = 0; i < theList.length(); ++i)
    {
        cout << theList.getValue() << " ";

        theList.next();
    }
    cout << "\n";

    // remove two elements at the specified position
    theList.moveToPos(5);
    cout << theList.currPos() << "\n";

    theList.remove();
    theList.remove();

    // display the contents of the list
    theList.moveToStart();
    for (i = 0; i < theList.length(); ++i)
    {
        cout << theList.getValue() << " ";

        theList.next();
    }
    cout << "\n";




    return 0;
}



