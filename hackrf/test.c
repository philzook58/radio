#include <hackrf.h>

static hackrf_device* device = NULL;
const char* serial_number = NULL;


int main(int argc, char** argv) {

  int result;
  result = hackrf_init();

  if( result != HACKRF_SUCCESS ) {
		printf("hackrf_init() failed:");
		//usage();
		return EXIT_FAILURE;
	}

  result = hackrf_open_by_serial(serial_number, &device);
  result = hackrf_set_sample_rate_manual(device, sample_rate_hz, 1);
  result = hackrf_set_vga_gain(device, vga_gain);
	result |= hackrf_set_lna_gain(device, lna_gain);
	result |= hackrf_start_rx(device, rx_callback, NULL);

  /* // Transmission
  result = hackrf_set_txvga_gain(device, txvga_gain);
		result |= hackrf_start_tx(device, tx_callback, NULL);
    /*/

result = hackrf_close(device);


}



int rx_callback(hackrf_transfer* transfer) {
	size_t bytes_to_write;
	int i;

	if( fd != NULL )
	{
		ssize_t bytes_written;
		byte_count += transfer->valid_length;
		bytes_to_write = transfer->valid_length;
		if (limit_num_samples) {
			if (bytes_to_write >= bytes_to_xfer) {
				bytes_to_write = bytes_to_xfer;
			}
			bytes_to_xfer -= bytes_to_write;
		}
		if (receive_wav) {
			/* convert .wav contents from signed to unsigned */
			for (i = 0; i < bytes_to_write; i++) {
				transfer->buffer[i] ^= (uint8_t)0x80;
			}
		}
		bytes_written = fwrite(transfer->buffer, 1, bytes_to_write, fd);
		if ((bytes_written != bytes_to_write)
				|| (limit_num_samples && (bytes_to_xfer == 0))) {
			return -1;
		} else {
			return 0;
		}
	} else {
		return -1;
	}
}
