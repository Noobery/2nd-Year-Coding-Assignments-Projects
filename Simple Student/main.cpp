#include <iostream>
#include <fstream>
#include <string>
#include <conio.h>

using namespace std;

const int MENU_INPUT = 1;
const int MENU_SHOW = 2;
const int MENU_DELETE = 3;
const int MENU_EDIT = 4;
const int MENU_SEARCH = 5;
const int MENU_EXIT = 6;

class Student{

    private:

        string firstName;
        string middleName;
        string lastName;
        string course;
        string idNumber;


    public:

        void displayMenu ();

        void inputMenu();
        void addStudent();
        void addCourse();

        void showMenu();
        void showStudent();
        void showCourse();

        void editStudent();

        void searchStudent();

        void deleteMenu();
        void deleteStudent();
        void deleteCourse();
};

void Student::displayMenu(){
    menuStart:
    int choice;
    system ("cls");

    cout<<"SIMPLE STUDENT INFORMATION SYSTEM"<<endl<<endl;
    cout<<"1. Create Student or Course"<<endl;
    cout<<"2. Show Student or Course List "<<endl;
    cout<<"3. Delete Student or Course"<<endl;
    cout<<"4. Edit Student Data"<<endl;
    cout<<"5. Search Student Data"<<endl;
    cout<<"6. Exit"<<endl;

    cout<<"\nEnter number: ";

    if (!(cin >> choice)) {
        cin.clear();
        cin.ignore();
        goto menuStart;
    }

    switch (choice){
        case MENU_INPUT:
            inputMenu();
            break;
        case MENU_SHOW:
            showMenu();
            break;
        case MENU_DELETE:
            deleteMenu();
            break;
        case MENU_EDIT:
            editStudent();
            break;
        case MENU_SEARCH:
            searchStudent();
            break;
        case MENU_EXIT:
            exit(0);
        default:
            cout<<"\nInvalid Number Please Try Again"<<endl;
            cout << "PRESS ANY KEY TO CONTINUE...";
            break;
    }

    getch ();
    goto menuStart;
}

void Student::inputMenu(){
    menuStart:
    int choice;
    system ("cls");

    cout<<"CREATE INFORMATION/DATA IN THE SYSTEM"<<endl;
    cout<<"\n1. Create Student Information"<<endl;
    cout<<"2. Add Course"<<endl;
    cout<<"3. Back"<<endl;


    cout<<"\nEnter number: ";

    if (!(cin >> choice)) {
        cin.clear();
        cin.ignore();
        goto menuStart;
    }

    switch (choice){
        case 1:
            addStudent();
            break;
        case 2:
            addCourse();
            break;
        case 3:
            displayMenu();
            break;
        default:
            cout<<"\nInvalid Number Please Try Again"<<endl;
            cout << "PRESS ANY KEY TO CONTINUE...";
            break;
    }

    getch ();
    inputMenu();
}

void Student::showMenu(){
    menuStart:
    int choice;
    system ("cls");

    cout<<"SHOW INFORMATION OF STUDENTS"<<endl;
    cout<<"\n1. Show Info of Students"<<endl;
    cout<<"2. Show List of Available Course"<<endl;
    cout<<"3. Back"<<endl;


    cout<<"\nEnter number: ";

    if (!(cin >> choice)) {
        cin.clear();
        cin.ignore();
        goto menuStart;
    }

    switch (choice){
        case 1:
            showStudent();
            break;
        case 2:
            showCourse();
            break;
        case 3:
            displayMenu();
        default:
            cout<<"\nInvalid Number Please Try Again"<<endl;
            cout << "PRESS ANY KEY TO CONTINUE...";
            break;
    }

    getch ();
    showMenu();
}

void Student::deleteMenu(){
    menuStart:
    int choice;
    system ("cls");

    cout<<"DELETE INFORMATION/DATA IN THE SYSTEM"<<endl;
    cout<<"\n1. Delete Student Data"<<endl;
    cout<<"2. Delete Course Available"<<endl;
    cout<<"3. Back"<<endl;


    cout<<"\nEnter number: ";

    if (!(cin >> choice)) {
        cin.clear();
        cin.ignore();
        goto menuStart;
    }

    switch (choice){
        case 1:
            deleteStudent();
            break;
        case 2:
            deleteCourse();
            break;
        case 3:
            displayMenu();
        default:
            cout<<"\nInvalid Number Please Try Again"<<endl;
            cout << "\nPRESS ANY KEY TO CONTINUE...";
            break;
    }

    getch ();
    deleteMenu();
}



void Student::addCourse(){
    string confirmation;
    system("cls");
    fstream file;

    cout<<"INPUT COURSE YOU WANT ADDED IN THE SYSTEM"<<endl;

    // Prompt and validate Course
    while (true) {
        cout<<"\nEnter Course: ";
        cin.ignore();
        getline(cin, course);
        cout << "You entered: " << course << endl;
        cout << "Is this correct? (Y/N): ";
        getline(cin, confirmation);
        if (confirmation == "Y" || confirmation == "y") {
            break;
        }
    }


    file.open("AvailableCourses.txt", ios::app | ios::out);
    file<<course<<endl;
    file.close();

    cout<<"\n\nData Successfully Added!"<< endl;
    cout<<"PRESS ANY KEY TO CONFIRM ..."<<endl;

}


void Student::addStudent() {
    string confirmation;
    system("cls");
    fstream file;

    cout << "INPUT STUDENT DETAILS" << endl;

    // Prompt and validate Last Name
    while (true) {
        cout << "\nEnter Last Name: ";
        cin.ignore();
        getline(cin, lastName);
        cout << "You entered: " << lastName << endl;
        cout << "Is this correct? (Y/N): ";
        getline(cin, confirmation);
        if (confirmation == "Y" || confirmation == "y") {
            break;
        }
    }

    // Prompt and validate First Name
    while (true) {
        cout << "\nEnter First Name: ";
        getline(cin, firstName);
        cout << "You entered: " << firstName << endl;
        cout << "Is this correct? (Y/N): ";
        getline(cin, confirmation);
        if (confirmation == "Y" || confirmation == "y") {
            break;
        }
    }

    // Prompt and validate Middle Name
    while (true) {
        cout << "\nEnter Middle Name: ";
        getline(cin, middleName);
        cout << "You entered: " << middleName << endl;
        cout << "Is this correct? (Y/N): ";
        getline(cin, confirmation);
        if (confirmation == "Y" || confirmation == "y") {
            break;
        }
    }

    // Prompt and validate Course
    bool validCourse = false;
    while (!validCourse) {
        cout << "\nAvailable Courses:" << endl;
        file.open("AvailableCourses.txt", ios::in);
        if (!file.is_open()) {
            cout << "No available courses found." << endl;
            cout << "ADD COURSES FIRST TO PROCEED" << endl;
            return;
        }
        string courseLine;
        while (getline(file, courseLine)) {
            cout << courseLine << endl;
        }
        file.close();

        cout << "\nEnter Course: ";
        getline(cin, course);
        cout << "You entered: " << course << endl;
        cout << "Is this correct? (Y/N): ";
        getline(cin, confirmation);
        if (confirmation != "Y" && confirmation != "y") {
            continue;
        }

        // Check if entered course is in available courses file
        file.open("AvailableCourses.txt", ios::in);
        if (!file.is_open()) {
            cout << "No available courses found." << endl;
            return;
        }
        while (getline(file, courseLine)) {
            if (courseLine == course) {
                validCourse = true;
                break;
            }
        }
        file.close();
        if (!validCourse) {
            cout << "Invalid course entered. Please try again." << endl;
        }
    }

    // Prompt and validate ID Number
    while (true) {
        cout << "\nEnter ID Number: ";
        getline(cin, idNumber);
        cout << "You entered: " << idNumber << endl;
        cout << "Is this correct? (Y/N): ";
        getline(cin, confirmation);
        if (confirmation == "Y" || confirmation == "y") {
            break;
        }
    }
    file.open("StudentManagement.txt", ios::app | ios::out);
    file << lastName << endl << firstName << endl << middleName << endl << course << endl << idNumber << "\n";
    file.close();

    cout << "\nData Successfully Added!" << endl;
    cout << "PRESS ANY KEY TO CONFIRM ..." << endl;
}



void Student::showCourse(){

    system("cls");
    fstream file;

    int count = 1;

    cout<<"LIST OF AVAILABLE COURSES"<<endl;

    file.open("AvailableCourses.txt",ios::in);
        if(!file){
            cout<<"No Data Present ...";
            file.close();
    }

        else {

            while (getline(file, course)) {
            cout<<"\n Course #"<<count++<<endl;
            cout<<" "<< course<<endl;

            }

            if (count == 1) {
                cout << "No data present." << endl;
            }
                 else {
                    cout << "\nThe list ends here." << endl;
                 }


    }
    file.close();
    cout << "PRESS ANY KEY TO RETURN ..." << endl;

}


void Student::showStudent(){

    system("cls");
    fstream file;

    int count = 1;

    cout<<"LIST OF STUDENTS"<<endl;

    file.open("StudentManagement.txt",ios::in);
        if(!file){
            cout<<"No Data Present ...";
            file.close();
    }

        else {

            while (getline(file, lastName)) {
            getline(file, firstName);
            getline(file, middleName);
            getline(file, course);
            getline(file, idNumber);

            cout<<"\n Student #"<<count++<<endl;
            cout<<" "<<lastName;
            cout<<", "<<firstName;
            cout<<" "<<middleName<<endl;
            cout<<" "<< course<<endl;
            cout<<" "<<idNumber<<endl;
            }

            if (count == 0) {
                cout << "No data present." << endl;
            }
                 else {
                    cout << "\nThe list ends here." << endl;
                 }


    }
    file.close();
    cout << "PRESS ANY KEY TO RETURN ..." << endl;

}



void Student::editStudent() {
    system("cls");
    ifstream file("StudentManagement.txt");
    ofstream newFile("temp.txt");

    int choice;
    string id;

    bool found = false;
    bool validCourse = false;
    string searchInput;


    cout << "EDIT STUDENT DETAILS" << endl;
    cout << "\n1. Modify Student Details" << endl;
    cout << "2. Back" << endl;
    cout << "\nEnter Number: ";
    cin.ignore();
    getline(cin, searchInput);

    if (!file) {
        cout << "No Data Present ..." << endl;
        return;
    }


    else if (searchInput == "1"){

    file.clear();
    file.seekg(0, ios::beg);

    cout << "\nEnter the ID number of the student to edit: ";
    getline(cin, id);

    while (getline(file, lastName)) {
        getline(file, firstName);
        getline(file, middleName);
        getline(file, course);
        getline(file, idNumber);

        if (idNumber == id) {
            found = true;

            cout<<"\nStudent Found"<<endl;
            cout<<"Name: "<<lastName<<", "<<firstName<<" "<<middleName<<endl;
            cout<<"Course: "<<course<<endl;
            cout<<"ID Number: "<<idNumber<<endl<<endl;


            cout << "Select the field to edit: " << endl;
            cout << "1. Last Name" << endl;
            cout << "2. First Name" << endl;
            cout << "3. Middle Name" << endl;
            cout << "4. Course" << endl;
            cout << "5. ID Number" << endl;
            cout<< "6. Back"<<endl;
            cout << "Enter choice: ";
            cin >> choice;
            cin.ignore();
            system("cls");

            switch (choice) {
                case 1:
                    cout<<"\nStudent Found"<<endl;
                    cout<<"Name: "<<lastName<<", "<<firstName<<" "<<middleName<<endl;
                    cout<<"Course: "<<course<<endl;
                    cout<<"ID Number: "<<idNumber<<endl<<endl;
                    cout << "Enter new last name: ";
                    getline(cin, lastName);
                    break;
                case 2:
                    cout<<"\nStudent Found"<<endl;
                    cout<<"Name: "<<lastName<<", "<<firstName<<" "<<middleName<<endl;
                    cout<<"Course: "<<course<<endl;
                    cout<<"ID Number: "<<idNumber<<endl<<endl;
                    cout << "Enter new first name: ";
                    getline(cin, firstName);

                    break;
                case 3:
                    cout<<"\nStudent Found"<<endl;
                    cout<<"Name: "<<lastName<<", "<<firstName<<" "<<middleName<<endl;
                    cout<<"Course: "<<course<<endl;
                    cout<<"ID Number: "<<idNumber<<endl<<endl;
                    cout << "Enter new middle name: ";
                    getline(cin, middleName);

                    break;
                case 4:

                while (!validCourse) {

                    cout<<"\nStudent Found"<<endl;
                    cout<<"Name: "<<lastName<<", "<<firstName<<" "<<middleName<<endl;
                    cout<<"Course: "<<course<<endl;
                    cout<<"ID Number: "<<idNumber<<endl;

                    cout << "\nAvailable Courses:" << endl;
                    fstream file("AvailableCourses.txt", ios::in);
                    if (file.is_open()) {
                        string courseLine;
                        while (getline(file, courseLine)) {
                            cout << courseLine << endl;
                        }
                        file.close();
                    } else {
                        cout << "No available courses found." << endl;
                    }

                    cout << "\nEnter new course: ";
                    getline(cin, course);
                    // Check if entered course is in available courses file
                    file.open("AvailableCourses.txt", ios::in);
                    if (file.is_open()) {
                        string courseLine;
                        while (getline(file, courseLine)) {
                            if (courseLine == course) {
                                validCourse = true;
                                break;
                            }
                        }
                        file.close();
                    } else {
                        cout << "No available courses found." << endl;
                    }

                    if (!validCourse) {
                        cout << "\nInvalid course entered. Please try again." << endl;
                    }
                }
                break;

                case 5:
                    cout<<"\nStudent Found"<<endl;
                    cout<<"Name: "<<lastName<<", "<<firstName<<" "<<middleName<<endl;
                    cout<<"Course: "<<course<<endl;
                    cout<<"ID Number: "<<idNumber<<endl<<endl;
                    cout << "Enter new ID number: ";
                    getline(cin, idNumber);
                    break;
                case 6:
                    displayMenu();
                    break;
                default:
                    cout << "Invalid choice. No changes were made" << endl;
                    break;
            }
        }

        newFile << lastName << endl << firstName << endl << middleName << endl << course << endl << idNumber << endl;
      }
    }
    else if (searchInput =="2"){
        displayMenu();
    }
    else {
        cout << "Invalid choice" << endl;
        cout<< "PRESS ANY KEY TO RETURN ...";
        return;
    }
    file.close();
    newFile.close();

    if (!found) {
        cout << "No record found with ID number " << id << endl;
        cout << "PRESS ANY KEY TO RETURN ..." << endl;
        remove("temp.txt");
        return;
    }
    cout << "SUUCESS, PRESS ANY KEY TO RETURN ..." << endl;
    remove("StudentManagement.txt");
    rename("temp.txt", "StudentManagement.txt");

}

void Student::searchStudent() {

    system("cls");
    ifstream file("StudentManagement.txt");
    string searchInput;
    bool found = false;

    cout << "SEARCH FOR STUDENT AND AVAILABLE COURSES:" << endl;
    cout << "\n1. Name" << endl;
    cout << "2. ID" << endl;
    cout << "3. Course" << endl;
    cout << "4. Back" << endl;
    cout << "\nEnter Number: ";
    cin.ignore();
    getline(cin, searchInput);

    if (!file) {
        cout << "No Data Present ..." << endl;
        return;
    }

    if (searchInput == "1") {
        string name;

        cout << "\nEnter the name of the student to search for: ";
        getline(cin, name);

        while (getline(file, lastName)) {
            getline(file, firstName);
            getline(file, middleName);
            getline(file, course);
            getline(file, idNumber);

            // Check if the input name is a substring of any of the name components
            if (lastName.find(name) != string::npos ||
                firstName.find(name) != string::npos ||
                middleName.find(name) != string::npos) {

                found = true;

                cout<<"\nStudent Found"<<endl;
                cout<<"Name: "<<lastName<<", "<<firstName<<" "<<middleName<<endl;
                cout<<"Course: "<<course<<endl;
                cout<<"ID Number: "<<idNumber<<endl;
            }
        }
    } else if (searchInput == "2") {
        string id;
        cout << "\nEnter the ID number of the student to search for: ";
        getline(cin, id);

        while (getline(file, lastName)) {
            getline(file, firstName);
            getline(file, middleName);
            getline(file, course);
            getline(file, idNumber);

            if (idNumber == id) {
                found = true;

                cout<<"\nStudent Found"<<endl;
                cout<<"Name: "<<lastName<<", "<<firstName<<" "<<middleName<<endl;
                cout<<"Course: "<<course<<endl;
                cout<<"ID Number: "<<idNumber<<endl;

                break;
            }
        }
    } else if (searchInput == "3") {
        string courseName;
        cout << "\nAvailable Courses:" << endl;
        ifstream courseFile("AvailableCourses.txt");
        if (courseFile.is_open()) {
            string courseLine;
            while (getline(courseFile, courseLine)) {
                cout << courseLine << endl;
            }
            courseFile.close();
        } else {
            cout << "No available courses found." << endl;
        }
        cout << "\nEnter the course name of the student to search for: ";
        getline(cin, courseName);

        file.clear();
        file.seekg(0, ios::beg);
        while (getline(file, lastName)) {
            getline(file, firstName);
            getline(file, middleName);
            getline(file, course);
            getline(file, idNumber);

            // Check if the input course name matches the course of the student
            if (course == courseName) {

                found = true;

                cout<<"\nStudent Found"<<endl;
                cout<<"Name: "<<lastName<<", "<<firstName<<" "<<middleName<<endl;
                cout<<"Course: "<<course<<endl;
                cout<<"ID Number: "<<idNumber<<endl;
            }
        }
    }
    else if (searchInput == "4"){
            displayMenu();

    }
     else {
        cout << "Invalid choice" << endl;
        cout<< "PRESS ANY KEY TO RETURN ...";
        return;
    }

    if (!found) {
        cout << "Student not found" << endl;
    }

    file.close();
    cout<<"\nPRESS ANY KEY TO RETURN ...";
}

void Student::deleteStudent() {
    system("cls");
    ifstream file("StudentManagement.txt");
    ofstream newFile("temp.txt");
    string id;
    bool found = false;

    cout << "DELETE EXISTING STUDENT INFORMATION "<<endl;
    cout << "\nEnter the ID number of the student to delete: ";
    cin.ignore();
    getline(cin, id);

    if (!file) {
        cout << "No Data Present ..." << endl;
        return;
    }

    while (getline(file, lastName)) {
        getline(file, firstName);
        getline(file, middleName);
        getline(file, course);
        getline(file, idNumber);

        if (idNumber == id) {
            found = true;
            cout << "\nName: " << lastName << ", " << firstName << " " << middleName << endl;
            cout << "Course: " << course << endl;
            cout << "ID Number: " << idNumber << endl;
            cout << "\nAre you sure you want to delete this record? (Y/N): ";
            string confirmation;
            getline(cin, confirmation);
            if (confirmation != "Y") {
                newFile << lastName << endl << firstName << endl << middleName << endl << course << endl << idNumber << endl;
                cout << "Student record not deleted." << endl;
            } else {
                cout << "Student record deleted." << endl;
            }
        } else {
            newFile << lastName << endl << firstName << endl << middleName << endl << course << endl << idNumber << endl;
        }
    }

    if (!found) {
        cout << "No matching student record found." << endl;
    }

    file.close();
    newFile.close();

    // Remove the old file and rename the new file
    remove("StudentManagement.txt");
    rename("temp.txt", "StudentManagement.txt");

    cout << "PRESS ANY KEY TO RETURN...";
}


void Student::deleteCourse() {
    string confirmation;
    system("cls");
    fstream coursesFile, studentsFile, tempCoursesFile, tempStudentsFile;

    cout << "DELETE AVAILABLE COURSES" << endl;

    // Prompt and validate Course to be deleted
    bool validCourse = false;
    while (!validCourse) {
        cout << "\nAvailable Courses:" << endl;
        coursesFile.open("AvailableCourses.txt", ios::in);
        if (coursesFile.is_open()) {
            string courseLine;
            while (getline(coursesFile, courseLine)) {
                cout << courseLine << endl;
            }
            coursesFile.close();
        } else {
            cout << "No available courses found." << endl;
        }

        cout << "\nEnter Course to Delete: ";
        cin.ignore();
        getline(cin, course);

        // Prompt for confirmation with loop to handle invalid input
        bool confirmed = false;
        while (!confirmed) {
            cout << "Are you sure you want to delete this course? (Y/N): ";
            getline(cin, confirmation);
            if (confirmation == "Y" || confirmation == "y") {
                confirmed = true;
            } else if (confirmation == "N" || confirmation == "n") {
                cout << "PRESS ANY KEY TO RETURN...." << endl;
                confirmed = true;
                return; // return to deleteMenu()
            } else {
                cout << "\nInvalid input. Please enter Y/N." << endl;
            }
        }

        // If confirmation is Y, continue with deleting the course and corresponding students
        coursesFile.open("AvailableCourses.txt", ios::in);
        tempCoursesFile.open("temp.txt", ios::app | ios::out);
        if (coursesFile.is_open() && tempCoursesFile.is_open()) {
            string courseLine;
            bool courseDeleted = false;
            while (getline(coursesFile, courseLine)) {
                if (courseLine == course) {
                    validCourse = true;
                    courseDeleted = true;
                } else {
                    tempCoursesFile << courseLine << endl;
                }
            }
            coursesFile.close();
            tempCoursesFile.close();
            remove("AvailableCourses.txt");
            rename("temp.txt", "AvailableCourses.txt");

            if (!courseDeleted) {
                cout << "\nInvalid course entered. Please try again." << endl;
            }
        } else {
            cout << "\nNo available courses found." << endl;
        }
    }

    // Delete students with the corresponding course from StudentManagement.txt
    studentsFile.open("StudentManagement.txt", ios::in);
    tempStudentsFile.open("temp.txt", ios::app | ios::out);
    bool deletedStudents = false;

    if (studentsFile.is_open() && tempStudentsFile.is_open()) {
        string lastName, firstName, middleName, studentCourse, idNumber;
        while (getline(studentsFile, lastName)) {
            getline(studentsFile, firstName);
            getline(studentsFile, middleName);
            getline(studentsFile, studentCourse);
            getline(studentsFile, idNumber);

            if (studentCourse != course) {
                tempStudentsFile << lastName << endl << firstName << endl << middleName << endl << studentCourse << endl << idNumber << endl;
            } else {
                deletedStudents = true;
            }
        }

        studentsFile.close();
        tempStudentsFile.close();
        remove("StudentManagement.txt");
        rename("temp.txt", "StudentManagement.txt");
    }

    cout << "\n\nData Successfully Deleted!" << endl;
    if (deletedStudents) {
        cout << "Students with the corresponding course have been deleted." << endl;
    } else {
        cout << "No students found with the corresponding course." << endl;
    }
    cout << "PRESS ANY KEY TO CONFIRM ..." << endl;
}



int main (){

    Student project;
    project.displayMenu();

    return 0;
}
