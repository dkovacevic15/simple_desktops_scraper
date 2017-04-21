STOP_IF_FOUND = True

import bs4, requests, os, gc

# Visit homepage
def visit(home_url: str, directory: str) -> None:
    print('All images will be downloaded to: ' + directory)
    print('Starting from url: ' + home_url)
    url = get_latest_post(home_url)
    while url:
        print('Analyzing url: ' + url)
        image_url_relative, url_of_previous_relative = get_urls(url)
        image_url = home_url + image_url_relative
        url_of_previous = home_url + url_of_previous_relative

        file_name = '_'.join((get_image_number(image_url), get_image_name(url)))
        file_name += '.png'

        download_image(image_url, directory, file_name)

        url = url_of_previous
        gc.collect()

def get_latest_post(home_url: str) -> (str, str):
    html_soup = get_soup(home_url)
    element = html_soup.select('.desktop a[href]')[0]
    relative_url = element.get('href')
    url = home_url + relative_url
    print('The latest post on the website is:\n' + url)
    print('\n\n')
    return url

def get_urls(url: str):
    html_soup = get_soup(url)
    image_url_relative = html_soup.select('.desktop a[href]')[0].get('href')
    url_of_previous_relative = html_soup.select('.back')[0].get('href')
    return image_url_relative, url_of_previous_relative

def get_soup(url: str):
    response = requests.get(url)
    response.raise_for_status()
    return bs4.BeautifulSoup(response.text, 'lxml')

def get_image_number(image_url: str) -> str:
    return image_url.split('=')[-1]

def get_image_name(url: str) -> str:
    return url.split('/')[-2]

def download_image(image_url, directory, file_name):
    filepath = os.path.join(directory, file_name)
    print('Downloading image from url: ' + image_url)
    print('Downloading image to path:  ' + filepath)
    print('\n')

    if os.path.exists(filepath):
        print('The image already exists. Assuming images are updated.')
        if STOP_IF_FOUND:
            print('Exiting.')
            quit()
        else:
            print('Skipping')
            return
    else:
        if not os.path.exists(directory):
            os.makedirs(directory)

    response = requests.get(image_url)
    response.raise_for_status()

    with open(filepath, 'wb') as destination_file:
        for chunk in response.iter_content(1024):
            destination_file.write(chunk)
    return


if __name__=='__main__':
    print('\n\n')
    visit('http://simpledesktops.com', os.path.join(os.getcwd(), 'simple_desktops'))
