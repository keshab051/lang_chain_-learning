from langchain_text_splitters import RecursiveCharacterTextSplitter

text = '''Lorem ipsum dolor sit amet, consectetur adipiscing elit. Vivamus lacinia odio vitae vestibulum vestibulum. Cras venenatis euismod malesuada. Nulla facilisi. Donec vulputate interdum sollicitudin. Nunc lacinia, nisl sit amet luctus porttitor, justo libero tincidunt magna, at dignissim sapien odio id nisi. Integer nec odio nec nulla luctus dignissim. Sed ut perspiciatis unde omnis iste natus error sit voluptatem accusantium doloremque laudantium, totam rem aperiam.

Eaque ipsa quae ab illo inventore veritatis et quasi architecto beatae vitae dicta sunt explicabo. Nemo enim ipsam voluptatem quia voluptas sit aspernatur aut odit aut fugit. Sed quia consequuntur magni dolores eos qui ratione voluptatem sequi nesciunt. Neque porro quisquam est qui dolorem ipsum quia dolor sit amet, consectetur, adipisci velit.'''

splitter = RecursiveCharacterTextSplitter(
    chunk_size = 400,
    chunk_overlap = 0
) 
print( splitter.split_text(text))


