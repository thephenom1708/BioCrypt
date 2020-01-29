//import com.machinezoo.sourceafis.FingerprintMatcher;
//import com.machinezoo.sourceafis.FingerprintTemplate;

import java.nio.file.Files;
import java.nio.file.Paths;
import java.util.*;

import java.awt.image.BufferedImage;
import java.io.File;
import javax.imageio.ImageIO;
import java.io.ByteArrayInputStream;

public class Test
{
    public static void main(String[] args) {
        
        /*byte[] probeImage = Files.readAllBytes(Paths.get("probe.png"));
        byte[] candidateImage = Files.readAllBytes(Paths.get("candidate.png"));

        FingerprintTemplate probe = new FingerprintTemplate(
            new FingerprintImage()
                .dpi(500)
                .decode(probeImage));

        FingerprintTemplate candidate = new FingerprintTemplate(
            new FingerprintImage()
                .dpi(500)
                .decode(candidateImage));

        double score = new FingerprintMatcher()
        .index(probe)
        .match(candidate);

        double threshold = 40;
        boolean matches = score >= threshold;

        System.out.println(matches);*/

        String url = "http://127.0.0.1:8000/apitest/returnShares/";
        String s1 = "";
        String param = "user_id=abc";
        HttpSendData send1=new HttpSendData(url, param);
        try
        {
            s1=send1.sendPOST();
        }
        catch (Exception e)
        {
            e.printStackTrace();
        }
        //System.out.println(s1.toString());    
        
        byte[] shareBytes = Base64.getDecoder().decode(s1.toString());
        ByteArrayInputStream bis = new ByteArrayInputStream(shareBytes);
        try{
            BufferedImage shareImage = ImageIO.read(bis);
            ImageIO.write(shareImage, "png", new File("/home/thephenom1708/output.png"));
        }
        catch(Exception e)
        {
            System.out.println(e.getMessage());
        }
        System.out.println("image created");

    }
}