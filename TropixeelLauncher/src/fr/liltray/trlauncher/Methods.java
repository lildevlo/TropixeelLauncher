package fr.liltray.trlauncher;

import java.io.File;
import java.io.FileInputStream;
import java.io.FileOutputStream;
import java.io.IOException;
import java.io.InputStream;
import java.net.URL;
import java.net.URLConnection;
import java.nio.file.Files;
import java.nio.file.Path;
import java.nio.file.Paths;
import java.nio.file.StandardCopyOption;
import java.util.zip.ZipEntry;
import java.util.zip.ZipInputStream;

public class Methods {
	
	public static void FilesLocations(){
		if (System.getProperty("os.name").startsWith("Windows")){
			new File("C:/TropixeelLauncher").mkdirs();
			new File("C:/TropixeelLauncher/Minecraft").mkdirs();
			
		   
		}
	}
	 public static void downloadZipFile() {
	        String saveTo = "C:/TropixeelLauncher/";
	        try {
	            URL url = new URL("https://download2279.mediafire.com/a6g2mbiil1xg/h7p0gm3s3hbsawh/repaths.zip");
	            URLConnection conn = url.openConnection();
	            InputStream in = conn.getInputStream();
	            FileOutputStream out = new FileOutputStream(saveTo + "launcherfiles.zip");
	            byte[] b = new byte[1024];
	            int count;
	            while ((count = in.read(b)) >= 0) {
	                out.write(b, 0, count);
	            }
	            out.flush(); out.close(); in.close();                   
	 
	        } catch (IOException e) {
	            e.printStackTrace();
	        }
	    }
	 
	 public static void extractzipfile() throws IOException{
		 
		  Path path = Paths.get("C:/TropixeelLauncher/launcherfiles.zip");
		  Path path1 = Paths.get("C:/TropixeelLauncher/Minecraft");
		  
		  unzipFolder(path, path1);
          System.out.println("Done");
	 }
	 public static void unzipFolder(Path path, Path path1) throws IOException {

	        try (ZipInputStream zis = new ZipInputStream(new FileInputStream(path.toFile()))) {

	            // list files in zip
	            ZipEntry zipEntry = zis.getNextEntry();

	            while (zipEntry != null) {

	                boolean isDirectory = false;
	                // example 1.1
	                // some zip stored files and folders separately
	                // e.g data/
	                //     data/folder/
	                //     data/folder/file.txt
	                if (zipEntry.getName().endsWith(File.separator)) {
	                    isDirectory = true;
	                }

	                

	                if (isDirectory) {
	                    Files.createDirectories(path);
	                } else {

	                    // example 1.2
	                    // some zip stored file path only, need create parent directories
	                    // e.g data/folder/file.txt
	                    if (path.getParent() != null) {
	                        if (Files.notExists(path.getParent())) {
	                            Files.createDirectories(path.getParent());
	                        }
	                    }

	                    Files.copy(zis, path, StandardCopyOption.REPLACE_EXISTING);

	                   
	                }

	                zipEntry = zis.getNextEntry();

	            }
	            zis.closeEntry();

	        }

	    }
	


	}