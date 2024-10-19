
-- Use the alx_book_store database
USE alx_book_store;

-- Show the structure of the books table
SELECT COLUMN_NAME, COLUMN_TYPE, DATA_TYPE FROM INFORMATION_SCHEMA.COLUMNS WHERE TABLE_SCHEMA = 'alx_book_store' AND TABLE_NAME = 'books';