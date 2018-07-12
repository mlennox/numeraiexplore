import imageio
import glob


def create_gif(target_file, source_folder, file_pattern):
    ""  ""
    filenames = [glob.glob(e) for e in (source_folder + '/' + file_pattern)]
    with imageio.get_writer(target_file, mode='I') as writer:
        for filename in filenames:
            image = imageio.imread(filename)
            writer.append_data(image)
