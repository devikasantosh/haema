# haema
Blood bank management system.
Created using Python, Tkinter, text files, and Python-MySQL connector.

There is a constant need for blood for patients during emergency situations or for a planned surgery. There is a constant shortage of availability of blood for donation. It is vital for the recipient that their blood group matches with the donor’s. Smooth functioning of blood banks would require meticulous record keeping. A software which performs this function of maintenance of record would be an essential tool for optimal utilisation of stored blood and for transfusion requirement.
This project, a software application called Haema, is created for blood bank administrators and managers to keep a record of their requests and stock, and to manage donations quickly and efficiently.
The objective is to keep this an extremely user-friendly and well-organised application.
The application provides a request form and a donation form, which can easily be filled in by blood bank personnel as and when they receive a new request or donation. The input is stored in a MySQL database.
The Management window is password-protected, and only the administrator can access this. This window displays the number of requests pending for each blood group, and the number of donated blood bags per group. The administrator can select a blood group and immediately receive information about which request needs to be filled first, and which donor’s blood must be given away first from this group. The process follows a first-in-first-out technique, where the oldest donated blood is given away first.
After the request is handled and the blood is allotted, the donor details are deleted from the Donor table in the database, and the number of blood bags in the Request table is decremented by one.
The application also provides assistance to users through features like Help, Frequently Asked Questions (FAQs), and contact details.
Haema is advantageous over manual record maintenance as a software-based application will always ensure minimising of manual errors. It also provides ease of data maintenance and data retrieval, with instant access to statistics relating to availability of blood and pending requests, thereby reducing the tedious manual process of data handling.
