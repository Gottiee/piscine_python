import shutil
import time

start_time = time.time()

def ft_tqdm(lst: range) -> None:

    size = len(lst)
    terminal_size = shutil.get_terminal_size().columns
    terminal_size -= 5 + 35

    for elem in lst:
        elem += 1
        print(elem, end="\r")
        porcent = elem * 100 / size
        fill = int((porcent * terminal_size / 100))
        if porcent > 99:
            fill = terminal_size
        loading = "█" * fill + " " * (terminal_size - fill)
        elapsed_time = time.time() - start_time
        estaming_time = (size - (elem + 1)) * (elapsed_time / (elem + 1))
        elapsed_min, elapsed_sec = divmod(elapsed_time, 60)
        iter_sec = (elem + 1) / elapsed_time
        estaming_min, estaming_sec = divmod(estaming_time, 60)
        if estaming_time <= 0:
            estaming_min, estaming_sec = (0 ,0)

        print(
            "{porcent:3.0f}%|{loading}| {elem}/{max_elem} [{m:02}:{s:02}<{mr:02}:{sr:02}, {iter:.2f}it/s]".format(
                porcent=porcent, loading=loading, elem=elem, max_elem=size,
                elapsed=elapsed_time, m=int(elapsed_min), s=int(elapsed_sec),
                mr=int(estaming_min), sr=int(estaming_sec), iter=iter_sec

            ),
            end="\r",
        )
        yield elem
