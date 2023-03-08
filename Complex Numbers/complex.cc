/*
CCC102 Laboratory Assignment No. 1
Due: May 23, 2022 (Monday) at 11:55PM

Provide the missing implementations of the complex number abstract data
type (ADT) in this file.

You must submit the whole homework package with your
modifications/additions in the electronic submission. This homework must
comply with the homework policy as stated in the "Assignments" page.
*/

#include <iostream>
#include <math.h>

#include "complex.hh"

using namespace std;



//Alrick Ivan A. Gicole - 2021-1283



// constructors
Complex::Complex(){ //default constructor
    _real=_imaginary=0;
 }
Complex::Complex(float real){ //constructor for real numbers
    _real=real;
    _imaginary=0;
 }
Complex::Complex(float real, float imaginary){
    _real=real;
    _imaginary=imaginary;
 }
Complex::Complex(const Complex &source){ //copy constructor
    _real=source._real;
    _imaginary=source._imaginary;
 }

 // accessor functions
float Complex::getReal() const{ //getter for real part
    return _real;
 }
float Complex::getImaginary() const{ //getter for imaginary part
    return _imaginary;
 }
void Complex::setReal(float real){ //setter for real part
    _real = real;
 }
void Complex::setImaginary(float imaginary){ //setter for imaginary part
    _imaginary = imaginary;
 }

// arithmetic operators
Complex operator +(const Complex &left, const Complex &right){
    Complex res;
    res.setReal(left.getReal()+right.getReal());
    res.setImaginary(left.getImaginary()+right.getImaginary());
    return res;
}
Complex operator -(const Complex &left, const Complex &right)
{
    Complex res;
    res.setReal(left.getReal()-right.getReal());
    res.setImaginary(left.getImaginary()-right.getImaginary());
    return res;
}
Complex operator *(const Complex &left, const Complex &right){
    Complex res;
    res.setReal(left.getReal()*right.getReal());
    res.setImaginary(left.getImaginary()*right.getImaginary());
    return res;
}
Complex operator /(const Complex &left, const Complex &right){
    Complex res;
    res.setReal(left.getReal()/right.getReal());
    res.setImaginary(left.getImaginary()/right.getImaginary());
    return res;
}

// assignment operators
Complex&Complex::operator =(const Complex &source){
    _real=source._real;
    _imaginary= source ._imaginary;
    return *this;
}
//shorthand assignment operators
Complex&Complex:: operator +=(const Complex &source){

    this->_imaginary+= source._imaginary;
    this->_real+= source._real;
    return *this;
}
Complex&Complex:: operator -=(const Complex &source){

    this->_imaginary-= source._imaginary;
    this->_real-= source._real;
    return *this;
}
Complex&Complex:: operator *=(const Complex &source){

    this->_imaginary*= source._imaginary;
    this->_real*= source._real;
    return *this;
}
Complex&Complex:: operator /=(const Complex &source){

    this->_imaginary/= source._imaginary;
    this->_real/= source._real;
    return *this;
}

// complex conjugate
Complex Complex:: conjugate() const{

    return Complex(_real, -1* _imaginary);
}

//complex inverse
 Complex Complex::inverse() const{
    Complex inv;
    inv.setReal(1 / _real);
    inv.setImaginary(1 / _imaginary);
    return inv;
 }

 //complex magnitude
 float Complex::magnitude() const{
    return sqrt(pow(_real,2)+pow(_imaginary,2));
 }

 //comparison operators
int operator == (const Complex &left, const Complex &right){
    return (left.getReal()==right.getReal() && left.getImaginary()==right.getImaginary());
}
int operator != (const Complex &left, const Complex &right){
    return (left.getReal()!=right.getReal() && left.getImaginary()!=right.getImaginary());
}
/*
Complete the implementation of the ADT for representing complex numbers
as declared in the header file "complex.hh" here. Implement the
constructors, the accessor functions, the assignment operators, the
complex conjugate method, the multiplicative inverse method, the complex
magnitude method, the arithmetic operators, and the comparison operators
of the Complex class. Read the class declaration in the header file
"complex.hh" for more information.
*/

/*
Implement the following functions in this file.

// constructors
Complex::Complex()
Complex::Complex(float real)
Complex::Complex(float real, float imaginary)
Complex::Complex(const Complex &source)

// accessor functions
float Complex::getReal() const
float Complex::getImaginary() const
void Complex::setReal(float real)
void Complex::setImaginary(float imaginary)

// assignment operators
Complex & Complex::operator =(const Complex &source)
Complex & Complex::operator +=(const Complex &source)
Complex & Complex::operator -=(const Complex &source)
Complex & Complex::operator *=(const Complex &source)
Complex & Complex::operator /=(const Complex &source)

// complex conjugate
Complex Complex::conjugate() const

// complex multiplicative inverse
Complex Complex::inverse() const

// complex magnitude
float Complex::magnitude() const

// arithmetic operators
Complex operator +(const Complex &left, const Complex &right)
Complex operator -(const Complex &left, const Complex &right)
Complex operator *(const Complex &left, const Complex &right)
Complex operator /(const Complex &left, const Complex &right)

// comparison operators
int operator == (const Complex &left, const Complex &right)
int operator != (const Complex &left, const Complex &right)
*/





/*
Stream input/output implementation:

The following stream inserter (<<) and extractor (>>) operators are
already implemented. You do not need to do anything to the
implementations. The implementations are designed to process complex
numbers in the format (real, imaginary).
*/

// stream inserter implementation
ostream & operator << (ostream &out, const Complex &value)
{
    // stream output of a complex number in the format
	// (real, imaginary)
    out << "(" << value.getReal() << ", " << value.getImaginary() <<
		")";

    return out;
}

// stream extractor implementation
istream & operator >> (istream &in, Complex &destination)
{
    // stream input of complex number
    float real = 0, imaginary = 0;

    char c;

    // read '('
    in >> c;
    if (c == '(')
    {
        // read real part
        in >> real;

        // read ','
        in >> c;
        if (c == ',')
        {
            // read imaginary part
            in >> imaginary;
        }
        else   // no imaginary part
        {
            in.putback(c);
        }

        // read ')'
        in >> c;
        if (c != ')')
        {
            in.putback(c);
        }
    }
    else // no imaginary part
    {
        in.putback(c);
        in >> real;
    }

    // do the assignment
    Complex result(real, imaginary);
    destination = result;

    // return the stream
    return in;
}
