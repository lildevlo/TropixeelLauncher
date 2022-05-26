package fr.liltray.trlauncher;

import java.io.File;
import java.io.IOException;

public class MainFrame {

	public static void main(String[] args) throws IOException {
		Methods.FilesLocations();
		Methods.downloadZipFile();
		Methods.extractzipfile();
	   }  
	}

