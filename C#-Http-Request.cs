using Flurl.Http; // download with nuget

var responseString = await "http://www.google.com".GetAsync();
Console.WriteLine(responseString.StatusCode);
Console.ReadKey();
