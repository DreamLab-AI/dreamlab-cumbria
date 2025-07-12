import React from 'react';
import { Button } from './ui/button';
import { Card, CardContent, CardDescription, CardHeader, CardTitle } from './ui/card';
import { Download, FileText } from 'lucide-react';
import { useToast } from './ui/use-toast';

export default function BrochureGenerator() {
  const { toast } = useToast();

  const downloadBrochure = () => {
    // Open the static HTML in a new tab for printing
    window.open('/dreamlab-brochure-printable.html', '_blank');
    
    toast({
      title: "Brochure Ready!",
      description: "Click 'Print as PDF' in the new tab to save the brochure.",
    });
  };

  return (
    <Card className="max-w-md mx-auto">
      <CardHeader>
        <CardTitle className="flex items-center gap-2">
          <FileText className="h-5 w-5" />
          DreamLab AI Brochure
        </CardTitle>
        <CardDescription>
          Download our professional brochure showcasing DreamLab AI's executive training services for the nuclear industry.
        </CardDescription>
      </CardHeader>
      <CardContent>
        <div className="space-y-4">
          <div className="text-sm text-muted-foreground">
            <p>The brochure includes:</p>
            <ul className="list-disc list-inside mt-2 space-y-1">
              <li>Executive training programs</li>
              <li>AI & VR technology overview</li>
              <li>Premium Lake District facility</li>
              <li>Investment opportunities</li>
              <li>Market analysis & projections</li>
            </ul>
          </div>
          
          <Button 
            onClick={downloadBrochure} 
            className="w-full"
          >
            <Download className="mr-2 h-4 w-4" />
            Download DreamLab AI Brochure
          </Button>
          
          <p className="text-xs text-muted-foreground text-center">
            Opens in a new tab. Click "Print as PDF" to save the brochure.
          </p>
        </div>
      </CardContent>
    </Card>
  );
}