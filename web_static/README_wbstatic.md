# web_static 

![page_exp](https://s3.amazonaws.com/intranet-projects-files/concepts/74/hbnb_step1.png)

# building a page
# resources

[Learn to Code HTML & CSS ](https://learn.shayhowe.com/html-css/building-your-first-web-page/)
[Inline Styles in HTML](https://www.codecademy.com/article/html-inline-styles)
[Specifics on CSS Specificity](https://css-tricks.com/specifics-on-css-specificity/)

# tasks 

# 0. Inline styling
![exemple_page](https://th.bing.com/th/id/OIP.QBs-VNGnV7FGe-EJevNGVQHaEf?pid=ImgDet&w=1219&h=739&rs=1)
``
explining the code
``

```html
<!DOCTYPE html>
```
- This line declares the document type and version of the HTML being used, which is HTML5.

```html
<html lang="en">
```
- This line begins the HTML document and specifies that the document's primary language is English.

```html
<meta charset="utf-8">
```
- This line sets the character encoding of the document to UTF-8, which is a standard character encoding for handling various characters and languages.

```html
<title>AirBnB Clone</title>
```
- This line sets the title of the webpage that will be displayed in the browser's title bar or tab. In this case, the title is set to "AirBnB Clone."

```html
<body style="margin: 0; padding: 0;">
```
- This line starts the body of the HTML document and applies inline CSS styling to the body element. It sets the margin and padding of the body to 0, effectively removing any default spacing around the body.

```html
<header style="background-color: #f00; height: 70px; width: 100%;">
</header>
```
- This block defines the header section of the webpage and applies inline CSS styling. It sets the background color of the header to red (#f00), height to 70 pixels, and width to 100% of the viewport width. However, there is no content inside the header in this code.

```html
<footer style="align-items: center;
               background-color: #0f0;
               bottom: 0;
               display: flex;
               height: 60px;
               justify-content: center;
               position: absolute;
               width: 100%;">
  Best School
</footer>
```
- This block defines the footer section of the webpage and applies inline CSS styling. It sets various styles for the footer, including vertical alignment (align-items: center), background color to green (#0f0), positioning at the bottom of the viewport (bottom: 0), flex display, a height of 60 pixels, horizontal centering of content (justify-content: center), absolute positioning, and a width of 100%.
- Inside the footer, the text "Best School" is placed. This text will be displayed in the center of the footer.

```html
</body>
</html>
```
- These lines close the body and HTML tags, respectively, ending the HTML document.

Overall, this HTML code creates a simple webpage with a red header and a green footer. The header spans the entire width of the viewport with a height of 70 pixels, while the footer is positioned at the bottom with a height of 60 pixels, containing the text "Best School" centered both vertically and horizontally. The body has no margins or padding.
