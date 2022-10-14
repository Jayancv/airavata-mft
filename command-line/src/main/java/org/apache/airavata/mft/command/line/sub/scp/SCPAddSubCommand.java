/*
 * Licensed to the Apache Software Foundation (ASF) under one or more
 * contributor license agreements.  See the NOTICE file distributed with
 * this work for additional information regarding copyright ownership.
 * The ASF licenses this file to You under the Apache License, Version 2.0
 * (the "License"); you may not use this file except in compliance with
 * the License.  You may obtain a copy of the License at
 *
 *     http://www.apache.org/licenses/LICENSE-2.0
 *
 * Unless required by applicable law or agreed to in writing, software
 * distributed under the License is distributed on an "AS IS" BASIS,
 * WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
 * See the License for the specific language governing permissions and
 * limitations under the License.
 */

package org.apache.airavata.mft.command.line.sub.scp;

import org.apache.airavata.mft.api.client.MFTApiClient;
import org.apache.airavata.mft.common.AuthToken;
import org.apache.airavata.mft.credential.stubs.scp.SCPSecret;
import org.apache.airavata.mft.credential.stubs.scp.SCPSecretCreateRequest;
import org.apache.airavata.mft.resource.service.scp.SCPStorageServiceGrpc;
import org.apache.airavata.mft.resource.stubs.scp.storage.SCPStorage;
import org.apache.airavata.mft.resource.stubs.scp.storage.SCPStorageCreateRequest;
import org.apache.airavata.mft.storage.stubs.storagesecret.StorageSecret;
import org.apache.airavata.mft.storage.stubs.storagesecret.StorageSecretCreateRequest;
import org.apache.airavata.mft.storage.stubs.storagesecret.StorageSecretServiceGrpc;
import picocli.CommandLine;

import java.util.concurrent.Callable;

@CommandLine.Command( name = "add" )
public class SCPAddSubCommand implements Callable<Integer>
{

    @CommandLine.Option( names = {"-n", "--user"}, description = "User Name" )
    private String user;

    @CommandLine.Option( names = {"-pr", "--private"}, description = "Private Key" )
    private String privateKey;

    @CommandLine.Option( names = {"-pu", "--public"}, description = "Public Key" )
    private String publicKey;

    @CommandLine.Option( names = {"-ph", "--passphrase"}, description = "Passphrase" )
    private String passphrase;


    @CommandLine.Option( names = {"-h", "--host"}, description = "Host" )
    private String host;

    @CommandLine.Option( names = {"-p", "--port"}, description = "Port" )
    private int port;

    @CommandLine.Option( names = {"-n", "--name"}, description = "Storage Name" )
    private String name;

    @CommandLine.Option( names = {"-s", "--storageId"}, description = "Storage ID" )
    private String storageId;

    @Override
    public Integer call() throws Exception
    {
        AuthToken authToken = AuthToken.newBuilder().build();

        MFTApiClient mftApiClient = MFTApiClient.MFTApiClientBuilder.newBuilder().build();

        SCPSecret scpSecret = mftApiClient.getSecretServiceClient().scp()
                .createSCPSecret( SCPSecretCreateRequest.newBuilder()
                        .setPrivateKey( privateKey )
                        .setPublicKey( publicKey )
                        .setPassphrase( passphrase )
                        .setUser( user )
                        .setAuthzToken( authToken ).build() );

        SCPStorageServiceGrpc.SCPStorageServiceBlockingStub scpStorageClient =
                mftApiClient.getStorageServiceClient().scp();
        StorageSecretServiceGrpc.StorageSecretServiceBlockingStub storageSecretClient =
                mftApiClient.getStorageServiceClient().storageSecret();

        SCPStorage scpStorage = scpStorageClient.createSCPStorage( SCPStorageCreateRequest.newBuilder()
                .setName( name )
                .setStorageId( storageId )
                .setUser( user )
                .setHost( host )
                .setPort( port )
                .build() );

        StorageSecret storageSecret = storageSecretClient.createStorageSecret( StorageSecretCreateRequest.newBuilder()
                .setStorageId( scpStorage.getStorageId() )
                .setSecretId( scpSecret.getSecretId() )
                .setType( StorageSecret.StorageType.SCP ).build() );

        System.out.println( "Storage Id " + scpStorage.getStorageId() );
        return 0;
    }
}
