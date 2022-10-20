const supabase = require("@supabase/postgrest-js");

const postgrest = new supabase.PostgrestClient("http:\/\/postgrest:3000");
module.exports = {
	db: postgrest,
	PostgrestClien : supabase.PostgrestClien
};
