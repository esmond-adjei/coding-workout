#include <iostream>

using namespace std;

/**
 * library class
 * - has books
 * - has shelves
 * - book
 * - user
 * - checkOut()
 * - checkIn()
 * - returnDate()
 *
 * user class
 * - libarian
 * - reader
 * 
 * books class
 * - book name
 * - book genre
 * - availablility
 * - bookCount
 */

class Book
{
private:
	string bookName_;
	string author_;
	string category_;
	int count_;
public:
	Book(string name, string author, string cat, int count);
	{
		setName(name);
		setAuthor(author);
		setCategory(cat);
		setCount(count);
	}
	
	string getName() { return bookName_;}
	string getAuthor() { return author_;}
	string setCategory() { return category_;}

	void setName(string name) { bookName_ = name;}
	void setAuthor(string author) { author_ = author; }
	void setCategory(string cat) { category_ = cat; }
	void setCount(int num) { count_ = num; }
	void addMoreBooks(int num) { count_ += num }
};


class User
{
private:
	string userName_;

public:
	User(string name): userName_(name) {}
	string getName() { return userName_; }
	void borrow(Book bk) { readBooks.push_back(bk); }
};


class Library
{
private:
	string libraryName_;
	vector<string> shelves_;
	vector<Book> allBooks_;
	vector<User> allUsers_;
	vector<Ledger> ledger_;


public:
	void checkIn(Book bkName, string category = '')
	{ 
		allBooks_.push_back(bkName);
		count_++;
	}

	void displayAllBooks()
	{
		for (auto book: allBooks_) { cout << book.getName() << endl; }
	}

	void displayByCat(string cat)
	{
		for (auto book: allBooks_)
		{
			if (book.getCategory() == cat) { cout << book.getName() << endl;}
		}
	}
	
	void checkOut(User user, Book bk)
	{
		ledger_.add(user, bk, bk.getCategory(), date);
	}

	void displayLedger()
	{
		for (auto ledger: ledger_) { ledger.display(); }
	}

};

class Ledger
{
	User userName_;
	Book book_;
	string category_;
	string date_;
	bool isReturned_;

	Ledger() {}
	void add(User username, Book bk, string cat, string date, bool isReturned)
	{
		userName_ = username;
		book_ = bk;
		category_ = cat;
		date_ = date;
		isReturned_ = isReturned;
	}

	display()
	{
		cout << userName_.getName() << " "
		     << book_.getName() << " "
		     << category_ << " " 
		     << date_ << " "
		     << isReturned_ << endl;
	}
};

int main()
{
	Library myLib;
	User user1;
	Book bk('book name', 'author', 'count');

	bk.count();

	myLib.checkIn(bk);
	myLib.displayAllBooks();
	myLib.displayByCat('category');
	myLib.checkOut(user1, bk);

	user1.borrow(bk);

	return (0);
}
