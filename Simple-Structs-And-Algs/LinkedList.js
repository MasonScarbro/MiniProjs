// ---------------------- LINKED LIST ---------------------- //


class Node {
    constructor(data, next = null) {
        this.data = data;
        this.next = next;
    }
}

class LinkedList {
    constructor() {
        this.head = null;
        this.size = 0;
    }

    // Insert first node, running this multiple times applies another node but it inserts only at the first meaning it pushes the initial first over
    // becuase we are creatign a new Node with the data but also the this.head as as the next and since this.head is assigned 
    // its assigning the las this.head as the next heres a rough diagram to explain I call insertFirst(100); this creates the head
    // with data: 100 and next set to the this.head which since this.head is activley being defined will be null
    // after ifi call insertFirst(200); it will actually push the previous head forward making it the next so 200 will be the head or the first node
    // hence the name basically its assining the previous node as next as you can tell by the params of the object 
    insertFirst(data) {
        this.head = new Node(data, this.head); 
        this.size++;
    }

    // Insert Last node 
    insertLast(data) { 
        let node = new Node(data);
        let current;
        
        //if empty make the head
        if (this.head == null) {
            this.head = node;
        } else {
            current = this.head;
            while (current.next) {
                current = current.next
            }
            current.next = node;
        }
        this.size++;
    }

    // Insert at Index
    insertAtIndex(data, index) {
        // If index is out of range
        if (index > 0 && index > this.size) {
            return;
        }
        // checking for the index at zero i.e insertfirst basically
        if (index == 0) {
            this.head = new Node(data, this.head)
            return;
        }

        const node =  new Node(data);
        let current, previous; // set current to the first for loop
        current = this.head;
        let count = 0;

        // Essintially what this is doing is setting the previous to the current and then counting so that 
        // the loop terminates before the index so that the previous is the well previous and the current is the one after
        // after the loop it will set the nodes next data to the current i.e the node after the previous and hten assing the node will be assigned to the previous node
        /*
            Lets go through with a visual example linked list is 2 -> 4 -> 6 -> 8
            and i want the value inserted at index 2. first current is assigned to value 2, index 0 the head
            and the loop runs 
            count = 0, previous = current i.e value 2, index 0
            count = 1, current = the next value i.e value 4, index 1
            count = 1, previous = value 4, index 1, current = the next value i.e value 6, index 2
            count = 2, Terminate loop

            node.next = current i.e value 6, index 2;
            previous.next (value 6, index 2) = node (99)
            new list = 2 -> 4 -> 99 -> 6 -> 8
        */
        while (count < index){
            previous = current; // Node before Index 
            current = current.next; // Node after the index 
            count++;
        }

        node.next = current; // new node next should the value of current 
        previous.next = node; //  This is basically setting the node to the actual index

        this.size++;
    }

    // Get at Index

    getAt(index) {
        let current = this.head;
        count = 0;
        while (current) {
            if (count == index){
                console.log(current.data)
                return current.data
            }
            count++;
            current = current.next;
        }
    }

    // Remove at Index
    removeAt(index) {
        if (index > 0 && index > this.size){
            return;
        }
        let current = this.head;
        let previous;
        let count = 0;

        if (index == 0) {
            this.head = current.next
        } else  {
            while (count < index){
                previous = current;
                current = current.next
                count++;
            }
            /* points the next node 2 -> 4 -> 6 -> 8 so if previous = 4 and current = 6  6 
            the new next pointer = 6 which we change to point to 8 effectivley 
            removing the next pointer for six ''severing the link'' */
            previous.next = current.next 
        }
        this.size--;
    }

    // Clear List
    clearList() {
        this.head = null;
        this.size = 0
    }

    sizeOf(){
        return this.size;
    }

    toString() {
        let current = this.head;
        let currentString = "";
        let count = 0;
        while(current){
            currentString += current.data + " -> "
            current = current.next
            count++;
            if (count == this.size - 1){ // basically checks if its the last data and if it is it just concatenates the last data so it doesnt have the arrow
                 currentString += current.data;
                 break;
            }
        }
        return currentString;
    }


}
const ll = new LinkedList();

insertFirst(400);
insertFirst(300);
insertFirst(200);
insertFirst(100);
insertAtIndex(250, 2);
console.log(ll.toString());
