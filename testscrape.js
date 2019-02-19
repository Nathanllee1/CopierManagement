<script type="text/javascript">
  const Http = new XMLHttpRequest();
  const url = 'https://10.99.21.243/job/JobSts_PrnJobSts_PrnJobs.htm?arg1=0&arg2=0&arg3=1&arg7=1&arg8=jobreset';

  Http.open("GET", url);
  Http.send();

  Http.onreadystatechange=(e)=>{
    console.log(Http.responseText)
  }
</script>
