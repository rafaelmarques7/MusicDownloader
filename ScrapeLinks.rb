require 'watir'
require 'Nokogiri'

artist_name = ARGV[0]
songs_path = ARGV[1]
link_path = ARGV[2]

search_base = 'https://www.google.pt/search?q='
search_final = '&tbm=vid'

songs = []
File.open(songs_path, 'r') do |f|
  f.each_line do |line|
    songs.push(line)
  end
end

browser = Watir::Browser.new(:phantomjs)

#clean file
File.open(link_path, 'w') { |f| f.write('') }
for song in songs
  search_url = search_base + artist_name.gsub(' ', '+') + song.gsub(' ', '+') + search_final
  browser.goto(search_url)
  sleep(1)
  data = Nokogiri::HTML.parse(browser.html)
  links = data.css('a').map { |link| link['href'] }
  link_list = []
  ss = 'www.youtube'
  #ss = 'url?q=https'
  for link in links
    if link.include? ss
      link_list.push(link)
    end
  end
  #File.open(link_path, 'a') { |f| f.write(link_list) }
  File.open(link_path, 'a') do |f|
    link_list.each { |link| f.puts(link) }
  end
end
