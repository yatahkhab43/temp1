#!/bin/bash

BOOK_FILE="address_book.txt"

create_book() {
    touch $BOOK_FILE
    echo "Address book created successfully"
}

view_book() {
    if [ -s $BOOK_FILE ]; then
        cat $BOOK_FILE
    else
        echo "Address book is empty"
    fi
}

insert_record() {
    echo "Enter name:"
    read name
    echo "Enter address:"
    read address
    echo "Enter phone:"
    read phone
    echo "$name:$address:$phone" >> $BOOK_FILE
    echo "Record inserted successfully"
}

delete_record() {
    echo "Enter name to delete:"
    read name
    if grep -q "^$name:" $BOOK_FILE; then
        sed -i "/^$name:/d" $BOOK_FILE
        echo "Record deleted successfully"
    else
        echo "Record not found"
    fi
}

modify_record() {
    echo "Enter name to modify:"
    read name
    if grep -q "^$name:" $BOOK_FILE; then
        delete_record
        insert_record
    else
        echo "Record not found"
    fi
}

while true; do
    echo -e "\nAddress Book Menu:"
    echo "1. Create address book"
    echo "2. View address book"
    echo "3. Insert a record"
    echo "4. Delete a record"
    echo "5. Modify a record"
    echo "6. Exit"
    echo "Enter your choice:"
    read choice

    case $choice in
        1) create_book ;;
        2) view_book ;;
        3) insert_record ;;
        4) delete_record ;;
        5) modify_record ;;
        6) exit 0 ;;
        *) echo "Invalid choice" ;;
    esac
done

chmod +x addressbook.sh
./addressbook.sh