//Programme returns the number of downloads from 
//a given github repository and given user name.

import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.net.HttpURLConnection;
import java.net.URL;
import java.util.Arrays;

public class gitHubAPI {
	public static void main(String[] args) throws Exception {

		String userName = "hartyp";
		String repoName = "CS3012AssignmentOne";
		HttpURLConnection connection = (HttpURLConnection) new URL(
				"https://api.github.com/repos/" + userName + "/" + repoName + "/releases").openConnection();
		BufferedReader input = new BufferedReader(new InputStreamReader(connection.getInputStream()));
		StringBuilder stringBuilderReturn = new StringBuilder();
		String line;
		while ((line = input.readLine()) != null) {
			stringBuilderReturn.append("\n" + line);
		}
		input.close();
		Arrays.stream(stringBuilderReturn.toString().split("\"download_count\":")).skip(1).map(l -> l.split(",")[0])
				.forEach(l -> System.out.println(l));
		int count = Arrays.stream(stringBuilderReturn.toString().split("\"download_count\":")).skip(1)
				.mapToInt(l -> Integer.parseInt(l.split(",")[0])).sum();
		System.out.println("Amount of downloads from user " + userName + "'s repository " + repoName + " is: " + count);

	}

}