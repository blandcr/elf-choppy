from elftools.elf.elffile import ELFFile

from contextlib import contextmanager

@contextmanager
def elf_file(elf_path):
    with open(elf_path, 'rb') as ff:
        yield ELFFile(ff)


def get_segments(elf_path, minimum_address_distance):
    with elf_file(elf_path) as elf:
        # Collect the segments we need
        segments = [segment for segment in elf.iter_segments()]

        # Prep the list of segments to be reduced
        segments = [list(segments[0])].extend(segments[1:])

        def stitch(stitched_segments, new_segment):
            farthest_address = stitched_segments[-1].header.p_paddr + stitched_segments[-1].header.p_filesz

        stitched_segments = reduce(stitch, segments)


