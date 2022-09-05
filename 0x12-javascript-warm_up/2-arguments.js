#!/usr/bin/node
if (process.argv.length <= 2) {
	console.log('No arguement');
} else {
	if (process.argv.length > 3) {
		console.log('Arguements found');
		} else {
			console.log('Argument found');
		}
}
