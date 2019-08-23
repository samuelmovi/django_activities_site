# Django Activities Site
This is a Django-based web application suitable for showcase. It's designed as a single-column commercial website for activities, but easily customizable

It's also multilingual, currently with support for English(default) and Spanish.

## Installation
For use in development, it required the following:

- Python 3.x
- Django: `pip install django`
- Postgresql docker image: `docker pull postgres:alpine`
- Postgresql client: `sudo apt install postgresql-client`

## Layout
- Contact bar: situated at the top, and populated with Contact entities. Sticky, collapsible, responsive.
- Carousel: a photo slide-show, populated with CarouselPhotos instances linked to the Page or Experience requested.
- Navigation Bar: first it shows links to all experiences, organized in dropdown-per-type, then all pages.
- Content 
- Footer: good place to put a contact form

## Models
There are 5 models in the app.

### Page
It has text field, which is displayed inside a frame

### Activity
It has a summary field, where the info on the activity in question, and a details field for all the minutia.

### Contact
Social media, email and telephone, with customized icons and links

### CarouselPhoto
If photos are loaded to the rendered template they will be rendered between the top contact bar and the navigation bar. For both Pages and Activities.

### Excerpt
The home page displays a grid of cards for curated content. When clicked a modal with an excerpt on the activity will be shown, with a link to the respective activity.

## Usage

## Steps
The included `STEPS.md` file is a compendium of the steps necessary to bring this project to a working order.

## Contributing
Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.

Please make sure to update tests as appropriate.
